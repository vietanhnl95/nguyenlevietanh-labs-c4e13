n = int(input("Enter a number: "))
count = 0
x = n

while x > 0:
    if n % x == 0:
        count += 1
    x = x - 1

if 0 < x and count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
