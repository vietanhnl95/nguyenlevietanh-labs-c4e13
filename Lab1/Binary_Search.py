numbers = [-123, -99, - 56, -23, -11, 9, 33, 36, 78, 91, 123]
x = int(input("Enter a number: "))

start = 0
found_index = - 1
stop = len(numbers) - 1
check_num = (start + stop) // 2

while stop != start:
    if x == numbers[check_num]:
        found_index = check_num
        break
    elif x < numbers[check_num]:
        stop = check_num
        check_num = (start + stop) // 2
    else:
        start = check_num
        check_num = (start + stop + 1) // 2
if found_index != -1:
    print("Found at:", found_index)
else:
    print("Not found")
