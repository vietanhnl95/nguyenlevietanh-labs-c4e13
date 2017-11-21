def eval(x, y, operation):
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y == 0:
            result = 'NaN'
        else:
            result = x / y
    return result

# x = 10
# y = 5
# operation = '+'
# r = eval(1,5,'-')
# print(r)

# s = eval()
#
# x = int(input("x = "))
# operation = input("Operation(+,-,*,/): ")
# y = int(input("y = "))
#
# if operation in ['+', '-', '*', '/']:
#     r = eval()
# else:
#     print("Operation not available")
#
# print("Result: ")
# print("{0} {1} {2} = {3}".format(x,operation,y,r))
