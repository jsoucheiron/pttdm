#!/usr/bin/env python

import inspect
import json
import sys
from functools import wraps
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.data import JsonLexer
from pygments.formatters import TerminalFormatter


def pprint(value):
    formatted_value = highlight(
        json.dumps(
            value,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        ),
        JsonLexer(),
        TerminalFormatter(bg='dark')
    )
    print(formatted_value)


def print_func(func):
    print("--- Code start ---")
    code = "".join(inspect.getsourcelines(func)[0][1:])
    print(highlight(code, PythonLexer(), TerminalFormatter(bg='dark')))
    print("--- Code end ---")


def print_func_result(func):
    print("--- Result start ---")
    result = func()
    if result is not None:
        print("Return value: {0}".format(result))
    print("--- Result end ---")


def index():
    r = ""
    for k in sorted(slides, key=slides.get):
        doc = inspect.getdoc(slides[k][0])
        if doc is not None and k.isdigit():
            r += "{}: {}\n".format(k, doc.split('\n')[0])
    return r


def slide(*args, **kwargs):
    def wrap(f):
        def wrapped_f():
            print_func(f)
            sys.stdin.readline()
            if kwargs.get('executable', False):
                print_func_result(f)
                sys.stdin.readline()
        return wrapped_f
    if len(args) == 1 and callable(args[0]):
        # No arguments, this is the decorator
        # Set default values for the arguments
        return wrap(args[0])
    else:
        # This is just returning the decorator
        return wrap


@slide
def start():
    """
    Good morning!
    Welcome to Python tips, tricks and dark magic
    I'm Jordi Soucheiron and I work @ serverdensity (blog.serverdensity.com),
    where we make an awesome SaaS tool to monitor servers and websites.
    Feel free to interrupt and ask anything during the talk
    You can reach me through:
      - @jordixou
      - jordi@soucheiron.cat

    You can download (and execute) this presentation from here:
    https://github.com/jsoucheiron/pycones-pttdm/
    """


@slide(executable=True)
def slide_1():
    """ Working with dictionaries
    """
    my_dict = {'my_key': 'my_value'}
    key = 'my_key'

    if key in my_dict:
        del my_dict[key]

    if key in my_dict:
        print(my_dict[key])
    else:
        print("default value")


@slide(executable=True)
def slide_1_1():
    """ Use pop to simplify key deletion. Just remember to add a default value
    to avoid KeyExceptions
    """
    my_dict = {
        'my_key': 'my_value',
        'my_other_key': 'my_other_value'
    }
    print(my_dict.pop('my_key', "I don't care if it doesn't exist"))
    print(my_dict.pop('my_key', "I don't care if it doesn't exist"))
    print(my_dict.pop('my_key', "I don't care if it doesn't exist"))
    pprint(my_dict)


@slide(executable=True)
def slide_1_2():
    """ Dictionaries have a get method. This method let's you use a optional d
    parameter with a default value of None. If you set d, if the key doesn't
    exist you'll get d.
    """
    my_dict = {
        'my_key': 'my_value'
    }
    print(my_dict.get('my_key', 'default value'))
    print(my_dict.get('my_missing_key', 'default value'))
    print(my_dict.get('my_missing_key'))


@slide
def slide_2():
    """ Let's talk about lists
    """


@slide(executable=True)
def slide_2_1():
    """ Negative indexes
    """
    my_list = [1, 2, 3, 4, 5]
    print(my_list[-1])


@slide(executable=True)
def slide_2_2():
    """ List slicing
    """
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = 1
    end = 8
    step = 2
    pprint(my_list[start:end:step])
    pprint(my_list[end:start:-step])
    pprint(my_list[::-1])


@slide(executable=True)
def slide_2_3():
    """ List zipping
    """
    my_list_1 = ['a', 'b', 'c', 'd', 'e']
    my_list_2 = [1, 2, 3, 4, 5]
    print(zip(my_list_1, my_list_2))
    pprint(dict(zip(my_list_1, my_list_2)))


@slide(executable=True)
def slide_3():
    """ Advanced "and" and "or" usage.

    When concatenated, "and" will give back the value
    of the first non-true operand or the last operand if all the operands
    are True.
    When concatenated, "or" will give back the last operand if all are False or
    the first True operand.
    """
    print("---and---")
    print(True and False and None)
    print(True and None and False)
    print(True and 1 and 10 < 20)
    print(True and 10 < 20 and 1)
    print("---or---")
    print(True or False or None)
    print(1 or None or False)
    print(False or None or 0)
    print(0 or None or False)


def my_wrong_append(value, my_list=[]):
    my_list.append(value)
    return my_list


def my_append(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list


@slide(executable=True)
def slide_4():
    """ Default arguments are only evaluated once
    Assume we have this method (we do):

def my_wrong_append(value, my_list=[]):
    my_list.append(value)
    return my_list

    What's going to happen?
    """

    pprint(my_wrong_append(1))
    pprint(my_wrong_append(2))


@slide(executable=True)
def slide_4_1():
    """ So... unless you're doing it on purpose
    We can take advantage of "or" and do this:

def my_append(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list

    And now?
    """

    pprint(my_append(1))
    pprint(my_append(2))


@slide(executable=True)
def slide_5():
    """ Unpacking
    """

    a = 'rules!'
    b = 'PyConES'

    a, b = b, a

    print("{0} {1}".format(a, b))


@slide(executable=True)
def slide_6():
    """ Exceptions

    Disclamer: DON'T EVER DO THIS. Unless:
      - You want everyone to hate you
      - You want the FSM to kill a kitten every time this code runs
    """

    try:
        """Some very dangerous stuff"""
    except:
        pass

    try:
        """Some very dangerous stuff"""
    except Exception:
        pass


@slide(executable=True)
def slide_6_1():
    try:
        try:
            raise KeyboardInterrupt()
        except Exception:
            print("We won't print this")
    except:
        print("We won't catch the exception with Exception.")
        print("KeyboardInterrupt is not a subclass of Exception")
        print("only non-system-exiting exceptions are.")
        print("But they are still exceptions and, therefore, can be captured")


@slide
def slide_6_2():
    """ Exceptions follow the following hierarchy:
    BaseException
     +-- SystemExit
     +-- KeyboardInterrupt
     +-- GeneratorExit
     +-- Exception
          +-- StopIteration
          +-- StopAsyncIteration
          +-- ArithmeticError
          ....
    """


@slide(executable=True)
def slide_7():
    """ Full try/except/else/finally flow
    """

    try:
        a = 0
    except ValueError:
        print("The exception won't be raised")
    else:
        print("We'll run the code in else if the exception is not raised")
    finally:
        print("and we'll always run finally (great for cleanup code)")


@slide(executable=True)
def slide_7_1():
    """ Weird try/except/else/finally flow considerations
    """

    try:
        a = 0
    except ValueError:
        print("The exception won't be raised")
    else:
        print("We'll run the code in else if the exception is not raised")
        return 1
    finally:
        print("and we'll always run finally even avoiding return calls")
        print
        return 2


def print_point(x, y):
    print("({0}, {1})".format(x, y))


@slide(executable=True)
def slide_8():
    """ Other unpacking tricks:
    We have this helper function:
def print_point(x, y):
    print("({0}, {1})".format(x, y))
    """

    point_a = (3, 4)
    point_b = {'y': 4, 'x': 3}

    print_point(3, 4)
    print_point(*point_a)
    print_point(**point_b)


@slide
def slide_8_1():
    """ The most usual place where this is used is in functions overwritten in
    child classes:

    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__(*args, **kwargs)
        ...

    """


@slide(executable=True)
def slide_9():
    """ Chaining comparisons
    """

    x = 15
    y = 2 * x
    print(10 < x < 20 < y < 50)
    print(20 < x > 10)


@slide
def slide_10():
    """In order to start a web file server on
    the current directory, simply run:
    python2.7 -m SimpleHTTPServer 5000
    or
    python3 -m http.server 5000
    """

@slide
def questions():
    """ That's all I have for now.
    If you have any questions I'll be happy to answer them :)

    Thanks to @itorres for the index code

    I based most of this talk from the stuff I got from here:
    http://www.siafoo.net/article/52
    https://docs.python.org/3/library/functions.html
    http://stackoverflow.com/questions/101268/hidden-features-of-python
    http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    """


@slide
def end():
    """ Thank you all!!!
    """


if __name__ == "__main__":
    next_slide = 'start'
    slides = {
        'start': (start, '1'),
        '1': (slide_1, '1.1'),
        '1.1': (slide_1_1, '1.2'),
        '1.2': (slide_1_2, '2'),
        '2': (slide_2, '2.1'),
        '2.1': (slide_2_1, '2.2'),
        '2.2': (slide_2_2, '2.3'),
        '2.3': (slide_2_3, '3'),
        '3': (slide_3, '4'),
        '4': (slide_4, '4.1'),
        '4.1': (slide_4_1, '5'),
        '5': (slide_5, '6'),
        '6': (slide_6, '6.1'),
        '6.1': (slide_6_1, '6.2'),
        '6.2': (slide_6_2, '7'),
        '7': (slide_7, '7.1'),
        '7.1': (slide_7_1, '8'),
        '8': (slide_8, '8.1'),
        '8.1': (slide_8_1, '9'),
        '9': (slide_9, '10'),
        '10': (slide_10, 'questions'),
        'questions': (questions, 'end'),
        'end': (end, 'exit'),
        'exit': (exit, None),
        '0': (exit, None)
    }
    while True:
        try:
            print("Slide({0}):".format(next_slide))
            user_input = sys.stdin.readline().strip('\n')
            if user_input == '':
                user_input = next_slide

            func, next_slide = slides.get(
                user_input,
                (None, next_slide)
            )
            if func is exit:
                sys.exit(0)
            elif func is not None:
                func()
            else:
                print("Slide '{0}' not found. Available_slides:\n{1}".format(
                    user_input,
                    index()
                ))
        except Exception:
            raise
        except:
            sys.exit(0)
