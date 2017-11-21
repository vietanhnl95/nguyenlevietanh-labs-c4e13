from random import *

def generate_quiz():
    x = randint(1,10)
    y = randint(1,10)
    op = choice(['+', '-', '*', '/'])
    er = randint(-1,1)
    true_result = int(eval("{0} {1} {2}".format(x,op,y)))
    result = true_result + er
    # print(type(result))
    return [x,y,op,result]

# print(generate_quiz())

def check_answer(x, y, op, result, user_choice):
    if user_choice:
        if int(eval("{0} {1} {2}".format(x,op,y))) == result:
            return True
        else:
            return False
    else:
        if int(eval("{0} {1} {2}".format(x,op,y))) == result:
            return False
        else:
            return True
