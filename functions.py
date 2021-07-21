def Addition(num1,num2):
    result = num1 + num2
    print("{0} + {1} = {2}".format(num1,num2,result))

def Subtraction(num1,num2):
    result = num1 - num2
    print("{0} - {1} = {2}".format(num1,num2,result))

def Multiplication(num1,num2):
    result = num1 * num2
    print("{0} * {1} = {2}".format(num1,num2,result))

def Division(num1,num2):
    if num2 ==0:
        print("Syntax Error")
    else:
        result = num1 / num2
        print("{0} / {1} = {2}".format(num1,num2,result))
