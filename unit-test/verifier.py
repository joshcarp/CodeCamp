"""
This module implements a test runner for the 'pytest' package.

The goal of this module is to create a program to verbosely and informatively provide feedback for tasks given to students learning python in an easy to use fashion.

Written by Haohan Liu for CodeCamp.
"""

# class imports
import pytest


class Verifier:
    """Simplify functionality from the pytest module."""
    def __init__(self, *test_files, flags=None):
        """Initialise class object and run verifier test files with flags if specified."""
        # set specified flags or initialise default flags
        self.setflags(flags=flags)

        # initialise test_files
        self.setfiles(*test_files)

        # if test_files are present, run verifier
        if self.files:
            self.run()

    def run(self):
        """Execute verifier.

        Current test_files and flags can be replaced by specifying new test_files and flags.
        """
        # run pytest
        pytest.main(self.flags + self.files)

    def setflags(self, *flag, flags=None):
        """Set verifier flags.

        Leave no args for default flags '-x -v'.
        """
        # default flags
        DEFAULT = ['-x', '-v']

        # ensure flags are only set with either method
        if flag and flags:
            raise Exception('*flag and flags= cannot be used concurrently.')

        # set new flags
        if flags:
            self.flags = flags
        if flag:
            self.flags = list(flag)
        else:
            self.flags = DEFAULT

    def setfiles(self, *test_files):
        """Set verifier test files."""
        self.files = []
        # verify file names and add to self.files
        for file in test_files:
            assert isinstance(file, str), "file names must be of type 'str'."

            # ensure file names are valid
            if not file.startswith('test_'):
                print("[NOTICE] file names must begin with 'test_' to conform with pytest test discovery standards. Test functions must also begin with 'test_' to ensure they are discovered by pytest.")

            if not file.endswith('.py'):
                file += '.py'

            # append to file list
            self.files.append(file)


if __name__ == '__main__':
    Verifier('test_verifier.py')
    pass
