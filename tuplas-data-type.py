
#1.- Las Tuplas no permiten asignación de elementos, como las creas así se usan
miTupla = ("Manzana", "Pera", "Uva")
#Esto no se puede: miTupla[0] = "Sandia

#2.-Puedo convertir una Tupla a una Lista
lConvertida = list(miTupla)
print(f"La colección {lConvertida} ahora es de tipo {type(lConvertida)})")