
"""
This module implements unit testing functionality for validation of output from the python CodeCamp program.

(Haohan Liu 2019-06)
"""


class UnitTest:
    """Implements unit testing functionality for user created methods and     functions."""

    def __init__(self, func_str, noPrint=False, returnOutput=False):
        """Initialise unit testing class with the function to test."""
        assert isinstance(func_str, str), "function input must be of type 'str'"
        self.func = func_str
        self.noPrint = noPrint
        self.returnOutput = returnOutput

        # class states
        self.isTesting = False

    def _nl_(self):
        """Print a new line."""
        print('\n', end='')

    def _hr_(self, key='=', width=80):
        """Print a horizontal rule of 'key=' characters 'width=' long."""
        print(key * width)

    # def _kw_handler_(self, key, val, **kwargs):
    #     """Check conditionality of keyword argument inputs concisely."""
    #     if key in kwargs and kwargs[key] == val:
    #         return True
    #     return False

    def _arg2str_(self, arg):
        """Return a string which properly formats variables for clear print output."""
        if isinstance(arg, str):
            return f"'{arg}'"
        else:
            return str(arg)

    def _args2str_(self, args):
        """Return a string containing comma separated items from argument list."""
        # return joined string of input arguments
        return ', '.join(self._arg2str_(x) for x in args)

    def _kwargs2str_(self, kwargs):
        """Return a string containing comma separated items from key argument list."""
        # return joined string of input key arguments
        return ', '.join(f"{k}={self._arg2str_(v)}" for k, v in kwargs.items())

    def _func2str_(self, args, kwargs):
        """Return a string representation of the function tested."""
        if args and kwargs:
            f_pstr = f"{self.func}({self._args2str_(args)}, {self._kwargs2str_(kwargs)})"
        elif args:
            f_pstr = f"{self.func}({self._args2str_(args)})"
        elif kwargs:
            f_pstr = f"{self.func}({self._kwargs2str_(kwargs)})"
        else:
            f_pstr = f"{self.func}()"
        return f_pstr

    def run(self, *args, **kwargs):
        """Run the function and print the function output given a set of arguments the function would naturally take.

        If a return value is desired, pass in key 'returnOutput=True'.
        """
        # evaluate the function with all args and kwargs
        f_str = f"{self.func}(*{args}, **{kwargs})"
        f_out = eval(f_str)

        # create function representation for print output
        f_pstr = self._func2str_(args, kwargs)

        # print output, if not explicitly disabled
        if not self.noPrint and not self.isTesting:
            print('>>> ', f_pstr)

            # handle printing of string types accurately
            print(self._arg2str_(f_out))
            self._hr_()

        # return output
        if self.returnOutput or self.isTesting:
            return f_out

    def test(self, expected_output, *args, **kwargs):
        """Test the function and compare the output to an expected correct output.

        The expected output is the first argument of the test() method. All other arguments will be passed onto the function tested.
        """
        # set class state
        self.isTesting = True

        # capture test output
        f_out = self.run(*args, **kwargs)

        # return state to default
        self.isTesting = False

        # grab print string of function input
        f_pstr = self._func2str_(args, kwargs)

        # print output, if not explicitly disabled
        if not self.noPrint:
            if f_out == expected_output:
                print('>>>', f_pstr, '[PASSED]')

            else:
                print('>>>', f_pstr, '[FAILED]')

                print(self._arg2str_(f_out))

                self._hr_(key='-')

                print(self._arg2str_(expected_output), '(EXPECTED)')

                self._hr_()

        # return test result in bool
        if f_out == expected_output:
            return True
        return False

    def evaluate(self, tests, testKey=None):
        """Evaluate a function's performance by running through a series of unit tests.

        These tests are stored in the form of a dictionary, where the key is the function argument input and the linked value is the expected result.

        A specific test can be chosen by inserting the relevant key into 'testKey='.

        If the input argument is a string, it must be encapsulated as expected of a string. E.g. "'text'".
        """
        # testing stats
        total_tests = len(tests.keys())
        passed_tests = 0

        # testing loop
        for args, expected in tests.items():
            # create equivalent function and execute
            f_str = f"{self.func}({args})"
            f_out = eval(f_str)

            # compare results
            if f_out == expected:
                print('>>>', f_str, '[PASSED]')
                passed_tests += 1
            # if failed, show details to user
            else:
                print('>>>', f_str, '[FAILED]')

                print('  [OUTPUT]', self._arg2str_(f_out))
                print('[EXPECTED]', self._arg2str_(expected))

                self._hr_(key='-')

        print(f"{passed_tests}/{total_tests} test(s) passed.")
        self._hr_()


# testing area
if __name__ == "__main__":
    def test_function(a, b=0, c=2):
        """Test function."""
        return (a, b, c)

    def test_function2(input):
        """Test function."""
        return input

    ut = UnitTest('test_function')
    ut.run(1, c=3)
    ut.run(10, 9, 8)
    ut.run(a=1, c='10')
    ut.run(a=1, c=['8']*3)

    ut2 = UnitTest('test_function2')
    ut2.test('text', 'text')

    ut2_tests = {"'text'": 'text', "'apple'": 'apple', 1: 1, 2: 3}
    ut2.evaluate(ut2_tests)
