from random import randint, choice
from calc_func import eval

def condition(error,user_input):
    if (error == 0 and user_input == 'T') or (error != 0 and user_input == 'F'):
        return "Correct"
    if (error != 0 and user_input == 'T') or (error == 0 and user_input == 'F'):
        return "Wrong"

count = 0
while count < 3:
    x = randint(1,15)
    y = randint(1,5)
    err = randint(-1,1)
    operation = choice(['+', '-', '*', '/'])

    r = eval(x,y,operation)
    result = r + err
    print("{0} {1} {2} = {3}".format(x,operation,y,result))

    user_input = input("True of False (T/F)? ").upper()


    x = condition(err,user_input)
    if x == 'Wrong':
        count += 1

    print(x)
    print('-' * 20)

else:
    print("GAME OVER")
