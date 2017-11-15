numbers = [1, 4, -2, 5, -10, 20, 125]

min_num = numbers[0]

for num in numbers:
    if num < min_num:
        min_num = num
print("Min number is", min_num)
