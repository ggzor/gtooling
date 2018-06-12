from itertools import chain
from re import compile

from utils.iterators import index
from utils.arguments.results import *

keyvaluepattern = compile(r"^(\S+)=(\S+)$")

def create_unrecognized_list(args, offset):
    def map_arg(t):
        i, arg = t
        match = keyvaluepattern.match(arg)

        if match:
            return (match[1], match[2])
        else:
            return ("Position {}".format(offset + i + 1), arg)

    return list(map(map_arg, index(args)))

def from_list(schema, ls):
    invalid = []
    duplicated = []
    unrecognized = []
    missing = []

    errors = []

    allArgsCount = len(schema.all_args)

    result = [None] * allArgsCount
    sources = list(map(lambda x: [], schema.all_args))
    def nextNoneIndex():
        for i in range(len(result)):
            if result[i] == None:
                return i

    names = [spec.name for spec in schema.all_args]

    toProcess = ls[:allArgsCount]
    extra = ls[allArgsCount:]

    def try_convert_and_set(index, spec, value):
        try:
            result[index] = spec.converter(value)
        except Exception as error:
            invalid.append((spec, str(error)))
            result[index] = value

    for arg in toProcess:
        i = nextNoneIndex()
        currentSpec = schema.all_args[i]
        match = keyvaluepattern.match(arg)

        if match:
            key, value = match[1], match[2]
            if key == currentSpec.name:
                sources[i].append(value)
                try_convert_and_set(i, currentSpec, value)
            else:
                if key in names:
                    nameIndex = names.index(key)

                    sources[nameIndex].append(value)
                    try_convert_and_set(nameIndex, schema.all_args[nameIndex], value)
                else:
                    unrecognized.append((key, value))
        else:
            sources[i].append(arg)
            try_convert_and_set(i, currentSpec, arg)

    for i, spec in index(schema.all_args):
        if result[i] == None:
            if spec.is_required():
                missing.append(spec)
            else:
                result[i] = spec.default

    for spec, argSources in zip(schema.all_args, sources):
        if len(argSources) > 1:
            duplicated.append((spec, argSources)) 

    unrecognized += create_unrecognized_list(extra, allArgsCount)

    if invalid:
        errors.append(InvalidArgs(invalid))

    if missing:
        errors.append(MissingArgs(missing))

    if duplicated:
        errors.append(DuplicatedArgs(duplicated))

    if unrecognized:
        errors.append(UnrecognizedArgs(unrecognized))

    if any(errors):
        return MergedResult(errors)

    return Success(result)