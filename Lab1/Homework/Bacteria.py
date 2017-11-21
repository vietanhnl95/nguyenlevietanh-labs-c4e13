x = int(input("How many B bacterias are there? "))
y = int(input("How much time in minutes will we wait? "))

for i in range(0,y,2):
    x = x * 2
print("After {0} minutes, we would have {1} bacterias".format(y,x))
