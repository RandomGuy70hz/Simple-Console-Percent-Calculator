
#* Simple Percent Calculator - python version 

# pseudo code attempt
'''
begin
    input x with string Enter first number
    input y with string Enter second number
    calculate percent -> x / y * 100
    result = "x out of y is percent%"
    display output
'''

import re
def calculate_percent():
    initiate = True
    while initiate:
        x = input('Enter first number: ')
        if re.match("[^\d]", x):
            print('Try again')
        else:
            y = input('Enter second number: ')
            if re.match("[^\d]", y):
                print('Try again')
            else:
                calculate_percent = int(x) / int(y) * 100 # check for errors, may conflict with funciton name
                result = f'{x} out of {y} is {calculate_percent}%'
                print(result)
                initiate = False

def greet():
    greeting = input(
"""
Howdy'

Would you like to get a percentage? 

Type y to continue... 
Press any other key to quit.

""")
    if greeting == 'y':
        calculate_percent()
        initiate = True
        while initiate:
            control = input(
"""
Would you like to do another? 

Type y to continue... 
Press any other key to quit.

""")
            if control == 'y':
                calculate_percent()
            else:
                print('Cya')
                initiate = False
                break
    else:
        print('Cya')
        initiate = False
        return

greet()







# import re
# re.match(["^\d+"], input)
