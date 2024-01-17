"""
Lab Car
"""
# Importar las bibliotecas necesarias
import csv  # Para manejar archivos CSV
import copy  # Para realizar copias de elementos en Python

# Definir un diccionario llamado 'myVehicle' con valores iniciales predeterminados
myVehicle = {
    "vin": "<empty>",
    "make": "<empty>",
    "model": "<empty>",
    "year": 0,
    "range": 0,
    "topSpeed": 0,
    "zeroSixty": 0.0,
    "mileage": 0
}

# Imprimir los valores iniciales del diccionario 'myVehicle'
for key, value in myVehicle.items():
    print("{} : {}".format(key, value))

# Crear una lista vacía llamada 'myInventoryList' para almacenar vehículos
myInventoryList = []

# Administrar el archivo CSV llamado 'car-fleet.csv'
with open('car-fleet.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  # Configurar el lector de CSV
    lineCount = 0  # Inicializar un contador de líneas

    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  # Imprimir nombres de columnas
            lineCount += 1
        else:
            # Imprimir información del vehículo desde el archivo CSV
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')

            # Crear una copia profunda del diccionario 'myVehicle' para almacenar los datos del vehículo actual
            currentVehicle = copy.deepcopy(myVehicle)
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]

            # Agregar el vehículo actual a la lista 'myInventoryList'
            myInventoryList.append(currentVehicle)
            lineCount += 1
    print(f'Processed {lineCount} lines.')

# Imprimir la información de los vehículos en 'myInventoryList'
for myCarProperties in myInventoryList:
    for key, value in myCarProperties.items():
        print("{} : {}".format(key, value))
        print("-----")