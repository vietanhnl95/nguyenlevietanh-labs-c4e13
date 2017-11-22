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
    true_result = int(eval("{0} {1} {2}".format(x,op,y)))
    if user_choice:
        return true_result == result
    else:
        return true_result != result
