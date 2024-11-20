from Vehiculo import *

# Función para crear una instancia de Automovil solicitando datos al usuario
def crear_automovil(numero): 
    print(f"\nIngrese los datos para el automóvil {numero}:")
    marca = input("Ingrese la marca del automóvil: ") 
    modelo = input("Ingrese el modelo del automóvil: ") 
    nro_ruedas = int(input("Ingrese el número de ruedas del automóvil: ")) 
    velocidad = int(input("Ingrese la velocidad del automóvil (Km/h): ")) 
    cilindrada = int(input("Ingrese la cilindrada del automóvil (cc): ")) 
    return Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)

# Función para crear una lista de Automoviles
def crear_automoviles(): 
    cantidad = int(input("¿Cuántos vehículos desea insertar? ")) 
    lista_autos = [] 
    for i in range(1, cantidad + 1): 
        auto = crear_automovil(i) 
        lista_autos.append(auto) 
    return lista_autos

# Crear y mostrar los automoviles
automoviles = crear_automoviles() 
print("\nImprimiendo por pantalla los Vehículos:\n")
for i, auto in enumerate(automoviles, start=1): 
    print(f"Datos del automóvil {i} : Marca {auto.marca}, Modelo {auto.modelo}, {auto.nro_ruedas} ruedas, {auto.velocidad} Km/h, {auto.cilindrada} cc")