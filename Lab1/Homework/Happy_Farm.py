mature = 1
newborn = 0
new_mature = 0

for i in range(5):
    total = mature + new_mature + newborn
    newborn = mature
    mature = mature + new_mature
    new_mature = newborn
    newborn = 0
    print("Month {0}: {1} pair(s) of rabbit".format(i,total))
