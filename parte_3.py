from Vehiculo import *
import csv

# Función guardar
def guardar_datos_csv(nombre_archivo, vehiculos):
    with open(nombre_archivo, "w", newline="") as archivo:
        archivo_csv = csv.writer(archivo)
        for vehiculo in vehiculos:
            clase = f"<class '{vehiculo.__class__.__module__}.{vehiculo.__class__.__name__}'>"
            atributos = str(vehiculo.__dict__) 
            archivo_csv.writerow([clase, atributos])

# Función recuperar
def recuperar_datos_csv(nombre_archivo):
    vehiculos = []
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for vehiculo in archivo_csv:
            vehiculos.append(vehiculo)
    return vehiculos

# Instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)
# Lista de Vehiculos
vehiculos = [particular, carga, bicicleta, motocicleta]

# Llamado a la función guardar datos
guardar_datos_csv("vehiculos.csv", vehiculos)

# Recuperar y mostrar el contenido guardado
automoviles = recuperar_datos_csv("vehiculos.csv")
for automovil in automoviles:
    print(automovil)

# Leer datos
def leer_datos_csv(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        archivo_csv = csv.reader(archivo)
        for fila in archivo_csv:
            clase, atributos_str = fila
            atributos = atributos_str 
            clase_nombre = clase.split('.')[-1][:-2] 
            print(f"Lista de Vehiculos {clase_nombre} {atributos}\n")

# Llamado a la función leer datos
leer_datos_csv("vehiculos.csv")