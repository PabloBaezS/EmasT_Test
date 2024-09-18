print("ingrese su palabra/frase para ver si es palindromo")
word = str(input())

word_no_blank_spaces = word.replace(" ","")

n = len(word_no_blank_spaces)

x = list(word_no_blank_spaces)

i = 0

if n%2 == 0:
    for i in range(int(n/2)):
        while True:
            if x[i] == x[n-1]:
                i+=1
            else:
                print("La palabra:", word, "No es palindromo")
                break
            print("La palabra:", word, "es palindromo!")
            break
        break
else:
    for i in range(int(n/2)-1):
        while True:
            if x[i] == x[n-1]:
                i+=1
            else:
                print("La palabra:", word, "No es palindromo")
                break
            print("La palabra:", word, "es palindromo!")
            break
        break




'''    true = True
    while true == True:
        if x[i] == x[n-1]:
            i+=1
            true = True
        else:
            print("La palabra:", word, "No es palindromo")
            true = False


for

    if true == True:
        print("La palabra:", word, "es palindromo!")
'''