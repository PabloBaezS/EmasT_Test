print("Ingrese su n:")
n = int(input())

x = []

a, b = 0, 1
for _ in range(n):
    x.append(a)
    a, b = b, a + b

print("la secuencia de fibonacci para n:", n, "es:",x)


