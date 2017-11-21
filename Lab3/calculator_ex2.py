print("Write a calculation: ", end ='')
cal = str(input())

# result = eval(cal)
# print(result)
content = cal.split()
print(content)
result =


if content[1] == '+':
    result = x + y
elif content[1] == '-':
    result = x - y
elif content[1] == '*':
    result = x * y
elif content[1] == '/':
    result = x / y
print("Result: ")
print("{0} {1} {2} = {3}".format(x,operation,y,result))
