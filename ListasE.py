# Lista
# dentro de [] y se separan sus elementos por ,
# prácticamente no tiene límite
# soporta variedad en los tipos de elementos
# es mutable: se puede modificar después de creada
# cuenta con varios métodos
# por defecto se mantiene el orden de inserción
# acepta duplicados


"""
Listas
Cambiar la película 3 por Mulan
Cambiar la película 20 por Star Wars
Imprimir la película 1
Imprimir todas las películas
"""
peliculas = [
    "Titanic",
    "Avatar",
    "El Padrino",
    "Pulp Fiction",
    "Forrest Gump",
    "Matrix",
    "Interestelar",
    "Jurassic Park",
    "La La Land",
    "Star Wars: Episodio IV - Una nueva esperanza",
    "Harry Potter y la piedra filosofal",
    "Los Vengadores",
    "Gladiador",
    "El Señor de los Anillos: La Comunidad del Anillo",
    "El Rey León",
    "Batman: El Caballero de la Noche",
    "E.T. el Extraterrestre",
    "Toy Story",
    "Mad Max: Furia en la carretera",
    "Inception",
    "El Resplandor",
    "El Silencio de los Corderos",
    "Coco",
    "Rocky",
    "La La Land",
    "Buscando a Nemo"
]

peliculas[2] = "Mulan"
peliculas[19] = "Star Wars"

print(f"La pelicula 1 de la Lista es {peliculas[0]}")

print(f"Todas las peliculas son: {peliculas}")



#Ejemplos
print("Otros ejemplos de Listas...")
estudiantes = ["Victor", "Mariana", "Raziel"]

print(estudiantes)

# la forma de acceder a los elementos es por índices
# el primer índice es el 0
# accedemos a un elemento nombredelalista[indice]

print("La segunda estudiante es "+estudiantes[2])

# len es una función que me da el tamaño de una lista, string, tupla, diccionario
n = len(estudiantes)

print(f"El tamaño de la lista es {n}")

# si quiero modificar un elemento lo referencio por el indice
estudiantes[0] = "Rodolfo"

print(estudiantes)