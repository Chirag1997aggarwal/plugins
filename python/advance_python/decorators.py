# Resource - https://www.python-engineer.com/courses/advancedpython/13-decorators/

# A decorator is a function that takes another function and extends the behavior of this function without explicitly modifying it. 
# It is a very powerful tool that allows to add new functionality to an existing function.
# There are 2 kinds of decorators: - Function decoratos - Class decorators

# example - 
import functools
def start_end_decorator_4(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@start_end_decorator_4
def add_5(x):
    return x + 5
result = add_5(10)
print(result)
print(add_5.__name__)
help(add_5)


# The final template for own decorators - 

import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Do something before
        result = func(*args, **kwargs)
        # Do something after
        return result
    return wrapper
