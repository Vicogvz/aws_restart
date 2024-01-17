"""
Conjuntos de Datos(set)
"""
### CONJUNTOS o SETS
# Se rige bajo la teoría de conjuntos
# no tienen orden
# son mutables
# no tienen repetidos
# sus elementos están dentro de {} y se separan por ,

print("\n\n\nSETS")

frutas = {"Manzana", "Pera", "Uva", "Pera"}

print(frutas)

comidas_mexicanas = [
    "Tacos",
    "Tamales",
    "Enchiladas",
    "Tacos",
    "Pozole",
    "Guacamole",
    "Chiles en Nogada",
    "Tamales",
    "Chiles Rellenos",
    "Sopes",
    "Pozole",
    "Tacos",
    "Enchiladas",
    "Chiles en Nogada",
    "Chiles Rellenos",
    "Tortas Ahogadas",
    "Tostadas",
    "Tacos",
    "Tlacoyos",
    "Sopes"
]


# Imprime las comidas sin repetidos
comidas_mexicanasSinRep = set(comidas_mexicanas)
print(comidas_mexicanasSinRep)
# Puedes acceder a las comidas de la lista utilizando índices, por ejemplo:
# print(comidas_mexicanas[0])   # Esto imprimirá "Tacos"

