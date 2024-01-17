"""
Diccionarios
"""
### DICCIONARIOS
# lógica Clave - Valor
# elemento {"clave": valor}
# los elementos están dentro de {} separados por comas
# la clave puede ser string o int
# valor puede ser de cualquier tipo de dato
# es mutable

print("DICCIONARIOS")

pelicula = {"nombre": "Titanic", "fecha": 1997, "Personajes":["Rose","Jack"]}

print(pelicula)

### Accedo a mis elementos por su clave
print("El nombre de la pelicula es",pelicula["nombre"])

# modificar un elemento
pelicula["fecha"] = 2000

print(pelicula)

numeros = {20: "Trabajadores"}
print(f"Diccionario de numero como clave",  numeros)
print(f"Elemento de un diccionario: {numeros[20]}")