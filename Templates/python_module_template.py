#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# Template Notes (remove this comment block from your own scripts/modules):
#
# The top line informs UNIX/LINUX that the current file should be executed
# as a python3 script. Unlike windows, which uses extensions like .doc or
# .pdf, file types are determined by their contents in Linux.
#
# In this course, we assume python3, rather than python2.
#
# The second top line informs python3 to use UTF-8 character encoding, which
# enables unicode characters as default instead of ASCII.
###

###
# Style Notes (remove this block from your own scripts/modules):
#
# Lines should never exceed 79 characters so that code is easily readable
# and printable. See the python style guide in the info repository for
# a complete guide on recommended coding practices.
#
# The comment block below is required according to Chapman University CPSC
# coding guidelines, also available in the info repository.
#
###


###
# Name: YOUR_FULL_NAME_HERE
# Student ID: ID_HERE
# Email: CHAPMAN_EMAIL_HERE
# Course: PHYS220/MATH220 Fall 2019
# Assignment: HOMEWORK_OR_CLASSWORK_NUMBER
###

"""
Module Description, one line summary

(Replace this docstring with your own documentation)
The first docstring at the top of the file appears in the "Description" field
of the help command. That is, if you load a python interpreter the following
makes the docstring visible:

  $ python
  >>> import your_module
  >>> help(your_module)

Note the name "your_module" above is the filename without the .py extension.
You can check this help for any python module (sys, numpy, sympy, etc.)
to get an idea about how module documentation is usually formatted, and what
information is usually included.

This docstring should contain an overview and purpose of the code being
written below, as well as example uses (if appropriate).
"""

# Place import statements here to load code from other modules
# DO NOT IMPORT MODULES THAT YOU DO NOT NEED
import numpy as np
import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt
import seaborn as sb
import numba as nb
# The above modules are commonly used for science. The "as blah"
# specification nicknames a module "blah" so you can write less
# in the rest of the module (e.g., np.array instead of numpy.array)


###
# Below is the body of the module.  Place all global constants, function
# definitions, and class definitions here.  No free-floating executable
# code should appear in a module.  Test functions should be placed in a
# separate file.
#
# All indentation should be 4 spaces!  NO TABS IN PYTHON CODE!
#
###


# When creating comments for your code, describe what you are trying to
# do at a high level. This helps guide the reader of your code to parse
# your intentions more easily. Don't describe exactly what the code does
# because that should be obvious from just reading the code.


# Put global constants at the top so they are easily found.
# Minimize the use of global constants if at all possible.
# Make global constants all capital with underscores by convention.
GLOBAL_CONSTANT_1 = 0


###
# If you are using object-oriented design, put class definitions next.
# For many scientific applications, object-oriented design may not be
# particularly advantageous, so we will not emphasize it in this course.
# For now it is safe to skip to the functions below.
###

class YourClass(object):
    """
    Class docstring, one line summary

    All classes should have their own documentation via docstrings.
    See the function docstring below for more detail.
    If a class does not subclass a particular other class, it should
    explicitly subclass the general class "object" as done above.
    All indentation should be 4 spaces.  NO TABS IN PYTHON CODE.
    Methods have their own docstrings (see below), so only include
    documentation about the attributes in the class docstring.

    Attributes
    ----------
        CONSTANT_ATTRIBUTE: float
            Describe attribute here, with type above
        variable_attribute: string
            One attribute description per line
    """

    # Class constant attributes should be capitalized with underscores
    CONSTANT_ATTRIBUTE = 3.14159265358

    # Class variable attributes should be lowercase with underscores
    variable_attribute = "change me at will"

    def __init__(self, *args, **kwargs):
        """
        Class constructor, one line summary

        Every class definition should have an __init__ method.
        All class methods should have their own docstrings as well.
        The first argument of every class method must be the special
        object "self", which will hold the current instance of the class.
        (This behavior is similar to 'this' in C++/Java if you are familiar.)

        The constructor initializes instance information using the arguments
        of the __init__ function. For example, class attributes may be set.

        Parameters
        ----------
            *args : types
                Descriptions here
            **kwargs : types (default: value), optional
                Descriptions here
        """
        # The "pass" keyword does nothing, so is useful when blocking
        # out intended code structure that has not yet been implemented.
        pass
    # Note that the method definition ends when the indendation returns to
    # its previous level of indentation

    def class_method(self, arg1, kwarg1="defaultvalue", *args, **kwargs):
        """
        Method docstring, one line summary

        A method is just a function that belongs to a class, so see
        below for detail about how functions work.

        Parameters
        ----------
            arg1 : type
            etc.
        """
        pass

# Note that the class definition ends when the indentation returns to the
# original indentation (which should be the far left of the file)


###
# Put function definitions after any class definitions.
# For most scientific work, creating a well-designed set of functions
# is often the best way to organize your tasks. Functions can be less
# rigid than classes to change and extend later. As such, functions
# should be your bread and butter for practical work.
###

def your_function(arg1, kwarg1="defaultvalue", *args, **kwargs):
    """
    Function docstring, one line summary

    All functions should have their own documentation via docstrings.
    Function arguments are positional, unless they are provided a default
    value to become a "keyword argument".
    Here args is a list of all positional arguments beyond those listed.
    Here kwargs is a list of all keyword arguments beyond those listed.

    The function doc string should describe the name of the function,
    its return value and type (if any), and its list of arguments and
    their expected types (if any). Both positional and keyword arguments
    should be listed separately.

    For more detailed examples from Google about how to use docstrings see,
    http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html

    All indentation should be 4 spaces.  NO TABS IN PYTHON CODE.

    Parameters
    ----------
        arg1 : type
            Describe the arguments of the function

        kwarg1: type (default: value), optional
            Describe keyword arguments of function

    Returns
    -------
        type :
            Describe the type and content of what the function returns here.
            It can be useful to give an example if the type is complicated.

    Raises
    ------
        If any exceptions can be raised by the function, describe them.
    """

    # Function body here - note the nice extra indented line for whitespace

    # The "return" keyword specifies the output of the function
    return return_value_goes_here


def your_generator(arg1, kwarg1="defaultvalue", *args, **kwargs):
    """
    Generator docstring, one line summary

    A generator is just a function that can pause its operation to
    return a value and then resume where it left off later.

    In python, the only difference is the replacement of the "return"
    keyword with the "yield" keyword.

    Parameters
    ----------
        arg1 : type
            Describe the arguments of the function

        kwarg1: type (default: value), optional
            Describe keyword arguments of function

    Yields
    -------
        type :
            Describe the type and content of what the generator yields here.

    Raises
    ------
        If any exceptions can be raised by the generator, describe them.
    """

    # Generator body here - note the nice extra indented line for whitespace

    # The "yield" keyword pauses the generator and returns an output.
    # The next time the generator is called, it resumes at the line after
    # the yield keyword. Very often yield statements are placed inside loops
    # so that many values can be returned in sequence as the generator is
    # called repeatedly.

    while True:  # By convention, this is how to create an infinite loop.
        yield return_value_goes_here


###
#
# After the body of the module, you can optionally create a protected main
# section to place executable scripting code. This main section should call
# the main function defined below.
#
# Importantly, all the above code consists of definitions, so it can be
# imported and used in other modules. Nothing executes by itself.
#
# Below is where we should place code that should be executed as a program.
#
###


def main(local_argv):
    """
    Main function

    See below for why this would exist. The local_argv argument lists command
    line arguments taken from sys.argv within the protected main block below.
    """
    # Perform executable tasks here
    pass


# Below is the python convention for defining an executable main section
if __name__ == "__main__":
    # This block only executes if the script is run as a standalone
    # program from the command line. Importantly is not run when
    # imported as a module.

    # It is convention to call a single function here if possible
    # This function should be defined above and house all code to be
    # executed. Operating system-specific modules that are needed only during
    # program execution should be imported here rather than at the top of the
    # module.

    # Note that the list sys.argv contains all commandline options.
    # The getopt module may also be helpful for more ambitious programs.
    import sys
    main(sys.argv)
