"""
Ejercicio 2: Calculadora de factorial

Escribe un programa que solicite al usuario un número entero no negativo y calcule su factorial. El factorial de un número entero positivo 'n' se define como el producto de todos los enteros desde 1 hasta 'n'. Utiliza un bucle para realizar el cálculo y muestra el resultado. Si el usuario ingresa un número negativo, muestra un mensaje de error y pide un número válido.

"""
numPositivo = int(input("Ingresa un número NO negativo: "))

while numPositivo < 0:
      print("El número que ingresaste {numPositivo} es negativo, intenta de nuevo")


vFactorial=1

 if numPositivo == 0:
     print(f"El factorial de 0 es 1:")
 elif numPositivo == 1:
     print(f"El factorial de 1 es {numPositivo}:")
 else:
     for i in range(1,numPositivo+1):
         print(f"Var i: {i}")
         vFactorial = i  * vFactorial
         print(f"Factorial: {vFactorial}")


"""
Ejercicio 3: Contador de números pares e impares

Escribe un programa que solicite al usuario un número entero positivo. Luego, utiliza un bucle para contar y mostrar la cantidad de números pares e impares en el rango desde 1 hasta el número ingresado por el usuario. Finalmente, muestra los resultados.

Por ejemplo, si el usuario ingresa el número 10, el programa debe mostrar algo como:

mathematica
Copy code
Números pares: 5
Números impares: 5
Este ejercicio te permitirá practicar el uso de bucles, condicionales y contar elementos en un rango.
"""
