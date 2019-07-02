"""
This module implements a test runner for the 'pytest' package.

The goal of this module is to create a program to verbosely and informatively provide feedback for tasks given to students learning python.
"""


class Verifier:
    """Abstract functionality from the pytest module."""
    def __init__(self, *test_files, flags=['-x', '-v'], ):
        """Execute verifier and sanitize inputs."""
        # class imports
        import pytest

        # class attributes
        self.files = []

        # verify file names
        for file in test_files:
            assert isinstance(file, str), "'test_files' item must be of type 'str'."

            # ensure file names are valid
            if not file.startswith('test_'):
                print("[NOTICE] file names must begin with 'test_' to conform with pytest test discovery standards. Test functions must also begin with 'test_' to ensure they are discovered by pytest.")

            if not file.endswith('.py'):
                file += '.py'

            self.files.append(file)

        self.result = pytest.main(flags + self.files)


if __name__ == '__main__':
    pass
