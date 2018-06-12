import pytest
from utils.arguments.schema import ArgsSchema, RequiredArg, OptionalArg
from utils.arguments.converters.numerics import to_integer, positive_integer_or_zero

description = "Simple description"
req1 = RequiredArg('req1', 
    description="Required arg 1"
)

req2 = RequiredArg('req2', 
    description="Required arg 2"
)

opt1 = OptionalArg('opt1', default=0, 
    description="Optional arg 1", 
    converter=[positive_integer_or_zero, to_integer]
)

opt2 = OptionalArg('opt2', default=[], 
    description="Optional arg 2",
    converter=lambda s: s.split(',')
)

allArgs = [req1, req2, opt1, opt2]

schema1 = ArgsSchema("test", description, allArgs)

class TestCorrectArgs:
    @pytest.mark.parametrize("arguments, expected", [
        (["s1", "s2"], ["s1", "s2", 0, []]),
        (["s1", "s2", "1"], ["s1", "s2", 1, []]),
        (["s1", "s2", "1", "x,d"], ["s1", "s2", 1, ["x", "d"]])
    ])
    def test_shouldBe_expected_when_argumentsAreJustPositional(self, arguments, expected):
        assert schema1.parse_list(arguments).args == expected

    @pytest.mark.parametrize("arguments, expected", [
        (["req1=s1", "req2=s2"], ["s1", "s2", 0, []]),
        (["req1=s1", "req2=s2", "opt1=1"], ["s1", "s2", 1, []]),
        (["req1=s1", "req2=s2", "opt2=x,d"], ["s1", "s2", 0, ["x", "d"]]),
        (["req1=s1", "opt1=1", "req2=s2", "opt2=x,d"], ["s1", "s2", 1, ["x", "d"]])
    ])
    def test_shouldBe_expected_when_argumentsAreKeyValue(self, arguments, expected):
        assert schema1.parse_list(arguments).args == expected

    @pytest.mark.parametrize("arguments, expected", [
        (["req1=s1", "s2"], ["s1", "s2", 0, []]),
        (["s1", "req2=s2", "1"], ["s1", "s2", 1, []]),
        (["s1", "s2", "opt1=1", "opt2=x,d"], ["s1", "s2", 1, ["x", "d"]]),
        (["s1", "s2", "opt2=x,d"], ["s1", "s2", 0, ["x", "d"]]),
        (["s1", "opt1=1", "s2", "opt2=x,d"], ["s1", "s2", 1, ["x", "d"]])
    ])
    def test_shouldBe_expected_when_argumentsAreMixedKeyValuePositional(self, arguments, expected):
        assert schema1.parse_list(arguments).args == expected

req3 = RequiredArg("req3", "Required arg 3")
schema2 = ArgsSchema("test", description, allArgs + [req3])

class TestIncorrectArgs:
    # pylint: disable=no-member
    @pytest.mark.parametrize("args, expected", [
        (["s1"], [req2, req3]), 
        (["req1=s1"], [req2, req3]),
        (["req2=s2"], [req1, req3]),
        (["opt1=1", "opt2=x,d"], [req1, req2, req3]),
        (["s1", "req2=s2"], [req3]),
        (["req1=s1", "s2"], [req3])
    ])
    def test_should_returnMissingArgs_when_missingRequiredArgs(self, args, expected):
        assert expected == schema2.parse_list(args).missing_args

    @pytest.mark.parametrize("args, expected", [
        (["s1", "s2", "s3", "1", "x,d", "extra1", "extra2"], [("Position 6", "extra1"), ("Position 7", "extra2")]),
        (["req1=s1", "req2=s2", "req3=s3", "extra1=e1"], [("extra1", "e1")]),
        (["s1", "s2", "s3", "extra1=e1"], [("extra1", "e1")]),
        (["req1=s1", "s2", "s3", "1", "x,d", "extra1"], [("Position 6", "extra1")])
    ])
    def test_should_returnUnrecognizedArgs_when_additionalArgs(self, args, expected):
        assert expected == schema2.parse_list(args).unrecognized_args

    @pytest.mark.parametrize("args, expected", [
        (["req1=s1", "req2=s2", "extra1=e1"], [req3, ("extra1", "e1")]),
        (["s1", "s2", "extra1=e1"], [req3, ("extra1", "e1")])
    ])
    def test_should_returnMissingAndUnrecognized_when_missingRequiredArgs_and_unrecognizedArgs(self, args, expected):
        result = schema2.parse_list(args)
        assert expected == result.missing_args + result.unrecognized_args

    @pytest.mark.parametrize("args, expected", [
        (["req1=s1", "req1=s1"], [(req1, ["s1", "s1"])]),
        (["s1", "s2", "req2=s3"], [(req2, ["s2", "s3"])]),
        (["s1", "s2", "opt1=0", "opt1=0"], [(opt1, ["0", "0"])])
    ])
    def test_should_returnDuplicates_when_duplicateArgs(self, args, expected):
        assert expected == schema2.parse_list(args).duplicated_args

    @pytest.mark.parametrize("args, expected", [
        (["s1", "s2", "s3", "a"], [(opt1, "The value 'a' is not a valid integer.")])
    ])
    def test_should_returnInconvertibleArgs_when_invalidArgsValues(self, args, expected):
        assert expected == schema2.parse_list(args).invalid_args