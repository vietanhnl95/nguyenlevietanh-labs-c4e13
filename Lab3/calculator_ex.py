x = int(input("x = "))
operation = input("Operation(+,-,*,/): ")
y = int(input("y = "))

if operation in ['+', '-', '*', '/']:
    if operation == '+':
        result = x + y
    elif operation == '-':
        result = x - y
    elif operation == '*':
        result = x * y
    elif operation == '/':
        if y = 0:
            result = 'NaN'
        else:
            result = x / y
else:
    print("Operation not available")

print("Result: ")
print("{0} {1} {2} = {3}".format(x,operation,y,result))
