print("Ingrese su n para FizzBuzz:")
n = int(input())
x = 1
for i in range(n):
    if x % 3 == 0 and x % 5 == 0 and x != 0:
        print("FizzBuzz")
    elif x % 3 == 0 and x != 0:
        print("Fizz")
    elif x % 5 == 0 and x != 0:
        print("Buzz")
    elif x != 0:
        print(x)
    x += 1
