numbers = [1,6,2,4,7,8,9,5,6,3,2,8,1,5,7,9,6,4,1,4]
print("This is the list of numbers:")
print(*numbers, sep=',')
x = int(input("Enter a number: "))

#not using count()
count_1 = 0
for num in numbers:
    if x == num:
        count_1 += 1
print("Number",x, "appear", count_1, "times in the list [This is not using count()]")

#using count()
count_2 = numbers.count(x)
print("Number",x, "appear", count_2, "times in the list [This is using count()]")
