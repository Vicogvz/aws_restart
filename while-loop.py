#Importando librerias
import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
print(number)

isGuessRight = False

#Indicar al usuario si el número es mayor o menor  
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        #isGuessRight = True
        #También podría usar break para salir del While
        break
    elif int(guess) > number:
        print(f"El número ingresado {guess} es mayor al número aleatorio. Intenta de nuevo")
    else:
        print(f"El número ingresado {guess} es menor al número aleatorio. Intenta de nuevo")
        
      