def get_even_list(l):
    even_list = []
    for number in l:
        if number % 2 == 0:
            even_list.append(number)
    return even_list

# input_list = [4,5,1,-2,5,6,2]
# print("Integer list: ", input_list)
# print("Even number list: ",get_even_list(input_list))

even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
