def remove_dollar_sign(s):
    return s.replace('$', '')

# s_input = str(input("Enter a string: "))
# print(remove_dollar_sign(s_input))
#
# print("-" * 15)
# print("Function checking")

string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
