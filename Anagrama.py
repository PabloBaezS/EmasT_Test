print("Ingresa palabra 1:")
palabra_1 = str(input())

print("Ingresa palabra 2:")
palabra_2 = str(input())

if sorted(palabra_1) == sorted(palabra_2):
    print("Es anagrama")
else:
    print("No es anagrama")


