#!/usr/bin/python

import inspect
import json
import sys
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.lexers.data import JsonLexer
from pygments.formatters import TerminalFormatter


def start():
    """
    Good morning!
    Welcome to Python tips, tricks and dark magic
    I'm Jordi Soucheiron and I work @ serverdensity, where we make an awesome
    SaaS tool to monitor servers and websites
    Feel free to interrupt and ask anything during the talk
    You can reach me through:
      - @jordixou
      - jordi@soucheiron.cat

    You can download (and execute) this presentation from here:
    https://github.com/jsoucheiron/pycones-pttdm/
    """


def slide_1():
    """ Working with dictionaries
    """
    my_dict = {'my_key': 'my_value'}
    key = 'my_key'

    if key in my_dict:
        del my_dict[key]

    if key in my_dict:
        print my_dict[key]
    else:
        print "default value"


def slide_1_1():
    """ Use pop to simplify key deletion. Just remember to add a default value
    to avoid KeyExceptions
    """
    my_dict = {
        'my_key': 'my_value',
        'my_other_key': 'my_other_value'
    }
    print my_dict.pop('my_key', "I don't care if it doesn't exist")
    print my_dict.pop('my_key', "I don't care if it doesn't exist")
    print my_dict.pop('my_key', "I don't care if it doesn't exist")
    pprint(my_dict)


def slide_1_2():
    """ Dictionaries have a get method. This method let's you use a optional d
    parameter with a default value of None. If you set d, if the key doesn't
    exist you'll get d.
    """
    my_dict = {
        'my_key': 'my_value'
    }
    print my_dict.get('my_key', 'default value')
    print my_dict.get('my_missing_key', 'default value')
    print my_dict.get('my_missing_key')


def slide_2():
    """ Let's talk about lists
    """


def slide_2_1():
    """ Negative indexes
    """
    my_list = [1, 2, 3, 4, 5]
    print my_list[-1]


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


def slide_2_3():
    """ List zipping
    """
    my_list_1 = ['a', 'b', 'c', 'd', 'e']
    my_list_2 = [1, 2, 3, 4, 5]
    print(zip(my_list_1, my_list_2))
    pprint(dict(zip(my_list_1, my_list_2)))


def slide_3():
    """ Advanced "and" and "or" usage.

    When concatenated, "and" will give back the value
    of the first non-true operand or the last operand if all the operands
    are True.
    When concatenated, "or" will give back the last operand if all are False or
    the first True operand.
    """
    print "---and---"
    print True and False and None
    print True and None and False
    print True and 1 and 10 < 20
    print True and 10 < 20 and 1
    print "---or---"
    print True or False or None
    print 1 or None or False
    print False or None or 0
    print 0 or None or False


def my_wrong_append(value, my_list=[]):
    my_list.append(value)
    return my_list


def my_append(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list


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


def slide_5():
    """ Unpacking
    """

    a = 'rules!'
    b = 'PyConEs'

    a, b = b, a

    print "{0} {1}".format(a, b)


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


def slide_6_1():
    try:
        try:
            raise KeyboardInterrupt()
        except Exception:
            print "We won't print this"
    except:
        print "We won't catch the exception with Exception."
        print "KeyboardInterrupt is not a subclass of Exception"
        print "only non-system-exiting exceptions are."
        print "But they are still exceptions and, therefore, can be captured"


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


def slide_7():
    """ Full try/except/else/finally flow
    """

    try:
        a = 0
    except ValueError:
        print "The exception won't be raised"
    else:
        print "We'll run the code in else if the exception is not raised"
    finally:
        print "and we'll always run finally (great for cleanup code)"


def slide_7_1():
    """ Weird try/except/else/finally flow considerations
    """

    try:
        a = 0
    except ValueError:
        print "The exception won't be raised"
    else:
        print "We'll run the code in else if the exception is not raised"
        return 1
    finally:
        print "and we'll always run finally even avoiding return calls"
        print
        return 2


def print_point(x, y):
    print "({0}, {1})".format(x, y)


def slide_8():
    """ Other unpacking tricks:
    We have this helper function:
def print_point(x, y):
    print "({0}, {1})".format(x, y)
    """

    point_a = (3, 4)
    point_b = {'y': 4, 'x': 3}

    print_point(3, 4)
    print_point(*point_a)
    print_point(**point_b)


def slide_8_1():
    """ The most usual place where this is used is in functions overwritten in
    child classes:

    def __init__(self, *args, **kwargs):
        super(MyClass, self).__init__(*args, **kwargs)
        ...

    """


def slide_9():
    """ Chaining comparisons
    """

    x = 15
    y = 2 * x
    print 10 < x < 20 < y < 50
    print 20 < x > 10


def slide_10():
    """In order to start a web file server on
    the current directory, simply run:
    python -m SimpleHTTPServer 5000
    """


def questions():
    """ That's all I have for now.
    If you have any questions I'll be happy to answer them :)

    I based most of this talk from the stuff I got from here:
    http://www.siafoo.net/article/52
    https://docs.python.org/3/library/functions.html
    http://stackoverflow.com/questions/101268/hidden-features-of-python
    http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
    https://docs.python.org/3/library/exceptions.html#exception-hierarchy
    """


def end():
    """ Thank you all!!!
    """


def pprint(value):
    formated_value = highlight(
        json.dumps(
            value,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        ),
        JsonLexer(),
        TerminalFormatter(bg='dark')
    )
    print formated_value


def print_func(func):
    print "--- Code start ---"
    code = "".join(inspect.getsourcelines(func)[0])
    print highlight(code, PythonLexer(), TerminalFormatter(bg='dark'))
    print "--- Code end ---"


def print_func_result(func):
    print "--- Result start ---"
    result = func()
    if result is not None:
        print "Return value: {}".format(result)
    print "--- Result end ---"


if __name__ == "__main__":
    next_slide = 'start'
    slides = {
        'start': (start, '1', False),
        '1': (slide_1, '1.1', True),
        '1.1': (slide_1_1, '1.2', True),
        '1.2': (slide_1_2, '2', True),
        '2': (slide_2, '2.1', False),
        '2.1': (slide_2_1, '2.2', True),
        '2.2': (slide_2_2, '2.3', True),
        '2.3': (slide_2_3, '3', True),
        '3': (slide_3, '4', True),
        '4': (slide_4, '4.1', True),
        '4.1': (slide_4_1, '5', True),
        '5': (slide_5, '6', True),
        '6': (slide_6, '6.1', False),
        '6.1': (slide_6_1, '6.2', False),
        '6.2': (slide_6_2, '7', True),
        '7': (slide_7, '7.1', True),
        '7.1': (slide_7_1, '8', True),
        '8': (slide_8, '8.1', True),
        '8.1': (slide_8_1, '9', False),
        '9': (slide_9, '10', True),
        '10': (slide_10, 'questions', False),
        'questions': (questions, 'end', False),
        'end': (end, 'exit', False),
        'exit': (exit, None, False),
        '0': (exit, None, False)
    }
    while True:
        try:
            print "Slide({0}):".format(next_slide)
            user_input = sys.stdin.readline().strip('\n')
            if user_input == '':
                user_input = next_slide

            func, next_slide, run = slides.get(
                user_input,
                (None, next_slide, False)
            )
            if func is exit:
                sys.exit(0)
            elif func is not None:
                print_func(func)
                sys.stdin.readline()
                if run:
                    print_func_result(func)
                    sys.stdin.readline()
            else:
                print "Slide '{0}' not found. Available_slides: {1}".format(
                    user_input,
                    sorted(slides.keys())
                )
        except Exception:
            raise
        except:
            sys.exit(0)
