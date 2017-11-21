numbers = [1, 4, -2, 5, -10, 20, 125]
x = int(input("Enter a number: "))

found_index = -1

for index,number in enumerate(numbers):
    if x == number:
        found_index = index

if found_index == -1:
    print("Not found")
else:
    print("Found", x ,"at", found_index)
