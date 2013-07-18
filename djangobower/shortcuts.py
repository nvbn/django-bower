import os


def is_executable(path):
    """Check file is executable"""
    return os.path.isfile(path) and os.access(path, os.X_OK)


def which(program):
    """
    Find by path and check exists.
    Analog of unix `which` command.
    """
    path, name = os.path.split(program)
    if path:
        if is_executable(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_executable(exe_file):
                return exe_file

    return None
