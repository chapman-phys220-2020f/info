#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Note: See python_module_template.py first

###
# Name: YOUR_FULL_NAME_HERE
# Student ID: ID_HERE
# Email: CHAPMAN_EMAIL_HERE
# Course: PHYS220/MATH220 Fall 2019
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER
###


# Many useful test functions are available in these modules
import nose.tools
import numpy.testing
# Look for the functions starting with "assert_" in each module
# Remember that you can use a python interpreter to see what they do
# For example:
#   >>> help(nose.tools.assert_almost_equal)


"""Test Module Description (Replace this docstring with your own documentation)

This docstring should contain an overview of the tests contained in the file.

All test modules should start with the prefix "test_" so that the "nose"
framework can locate which tests to run.
"""

# Test functions follow below
# For each logically independent test, write one test function.
# Each logical test may test multiple cases using multiple assert expressions.

def test_function_1():
    """Test function for nose

    Any function name starting with prefix "test_" will be automatically run
    by nose. Include docstrings for your tests so that nose can report
    information about the tests. Use function names that are themselves
    descriptive.

    In a test function, use an assert command to test a Boolean statement
    about the execution of your code.  If the assert fails, it throws
    an exception, which is caught by nose and reported as a failure.
    Anything that is printed to the screen during this function is
    suppressed unless there is a failure, where it can be used for
    debugging.
    """
    # Any print statements inside your test function will only be printed
    # in the event of a failure, and can be very useful for debugging

    print("Helpful test message")

    # This is an "assert" statement that uses the keyword "assert" like an
    # "if" test to check that an expression correctly evaluates to True.
    # If the if check fails, the "assert" expression throws an exception
    # and (optionally) prints the provided string for context.

    assert 2 == 1+1, "2 == 1+1"

    # You might consider using nose.tools.assert_equals(left_side, right_side)
    # instead of the raw assert command, since it gives more information
    # in the event of a failure

    nose.tools.assert_equals(2, 1+1)

    # When testing floating point numbers (with a decimal), always use
    # nose.tools.assert_almost_equals(left_side, right_side) instead to avoid
    # rounding errors (or alternatives in nose.tools or numpy.testing)


def test_function_2():
    """Second test for nose

    Each function is run as a separate logical test.
    """
    assert True
