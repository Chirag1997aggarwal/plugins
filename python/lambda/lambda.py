# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# Note :- lambda functions are just syntactic sugar for a normal function definition.

# Syntax -   lambda arguments : expression

# Pros -
# Good for simple logical operations that are easy to understand. This makes the code more readable too.
# Good when you want a function that you will use just one time.

# Cons -
# They can only perform one expression. It’s not possible to have multiple independent operations in one lambda function.
# Bad for operations that would span more than one line in a normal def function (For example nested conditional operations). If you need a minute or two to understand the code, use a named function instead.
# Bad because you can’t write a doc-string to explain all the inputs, operations, and outputs as you would in a normal def function.

list_1 = [1,2,3,4,5,6,7,8,9]
filter(lambda x: x%2==0, list_1)
# <filter at 0xf378982348>

list(filter(lambda x: x%2==0, list_1))
# [2, 4, 6, 8]

# With pandas apply functions
import pandas as pd
df = pd.DataFrame({
    'Name': ['Luke','Gina','Sam','Emma'],
    'Status': ['Father', 'Mother', 'Son', 'Daughter'],
    'Birthyear': [1976, 1984, 2013, 2016],
})

df['age'] = df['Birthyear'].apply(lambda x: 2021-x)

# Resources -
# https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8
