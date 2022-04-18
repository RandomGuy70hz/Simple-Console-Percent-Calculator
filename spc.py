
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
    freshstart = True
    while freshstart:
        x = input('Enter first number: ')
        if re.match("[^\d]", x):
            print('Try again')
        else:
            y = input('Enter second number: ')
            if re.match("[^\d]", y):
                print('Try again')
            else:
                my_percent = int(x) / int(y) * 100
                result = f'{x} out of {y} is {my_percent}%'
                print(result)
                freshstart = False

def user():
    greeting = input('Welcome. Would you like to get a percentage? ')
    if greeting == 'yes':
        calculate_percent()
        init = True
        while init:
            control = input('Would you like to do another? ')
            if control == 'yes':
                calculate_percent()
            else:
                print('Cya')
                init = False
                break
    else:
        print('Cya')
        init = False
        return

user()







# import re
# re.match(["^\d+"], input)
