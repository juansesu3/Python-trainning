'''utility of the function // own functions'''

"""Declaring the  function"""




from unittest import result
def mensaje():

    print("I'm the best")
    print("I'm the best")
    print("I'm the best")


"""Calling teh function """
print('First Call')
mensaje()
print('Second Call')
mensaje()


'''Addition & Asignation'''
"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
'''Function without parameters'''


def additionNotParameters():
    num1 = 10
    num2 = 10
    print("Function without parameters\n", num1+num2)


additionNotParameters()


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
'''Function with parameters'''


def additionYesParameters(num1, num2):

    print("Function with parameters\n", num1+num2)


additionYesParameters(10, 20)
additionYesParameters(20, 30)
additionYesParameters(50, 30)


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
'''Function with parameters and return'''


def additionReturnParameters(num1, num2):
    result = num1+num2
    return result


print("Funnction with return\n", additionReturnParameters(50, 80))


"""↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓"""
'''Funnction with return save in variable'''


def additionReturnParameters(num1, num2):
    result = num1+num2
    return result


result_saved = additionReturnParameters(80, 130)
print("Funnction with return save in variable\n", result_saved)











