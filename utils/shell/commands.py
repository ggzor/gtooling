from os import system

def do(command):
    """Executes the given command in the shell and returns its exit code."""
    return system(command)

def doAll(commands):
    """
    Executes all the given commands in the shell sequentially and conditionally.
    It will run the next command only if the previous one was successful. Returns
    0 if everything was OK, or a tuple of the form (command, exit code | exception)
    with the command that has failed. 
    """
    for command in commands:
        try:
            result = do(command)

            if result != 0:
                return (command, result)
        except Exception as ex:
            return (command, ex)

    return 0

def doEvery(commands):
    """
    Executes all the given comments in the shell in order and returns a list with
    tuples of the form (command, exit code | exception) for each command execution. 
    Use this method if the commands don´t depend on the execution of other.
    """
    results = []

    for command in commands:
        try:
            results += [do(command)]
        except Exception as ex:
            results += [ex]

    return results