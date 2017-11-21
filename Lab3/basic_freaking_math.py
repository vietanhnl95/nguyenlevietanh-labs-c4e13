from random import randint
from calculator_ex_function import eval

dead_count = 0

while dead_count < 3:
    x = randint(1,10)
    y = randint(1,10)
    err = randint(-2,2)
    result = x + y + err
    true_result = eval(x,y,'+')
    print("{0} + {1} = {2}".format(x,y,result))

    ans = input("(Y/N)? ")

    if err == 0 and ans.upper() == 'Y':
        print("Correct")
    elif err == 0 and ans.upper() == 'N':
        print("Wrong")
        dead_count += 1
    elif err != 0 and ans.upper() == 'Y':
        print("Wrong")
        dead_count += 1
    elif err != 0 and ans.upper() == 'N':
        print("Correct")
