from Vehiculo import *
    
# Instancias
particular = Particular("Ford", "Fiesta", 4, "180", "500", 5) 
carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000") 
bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera") 
motocicleta = Motocicleta("BMW", "F800s",2,"Deportiva","2T","Doble Viga", 21)

# Salida
print(f"Marca {particular.marca}, Modelo {particular.modelo}, {particular.nro_ruedas} ruedas, {particular.velocidad} Km/h, {particular.cilindrada} cc, Puestos: {particular.nro_puestos}")
print(f"Marca {carga.marca}, Modelo {carga.modelo}, {carga.nro_ruedas} ruedas, {carga.velocidad} Km/h, {carga.cilindrada} cc, Carga: {carga.peso_carga} Kg")
print(f"Marca {bicicleta.marca}, Modelo {bicicleta.modelo}, {bicicleta.nro_ruedas} ruedas, Tipo: {bicicleta.tipo}")
print(f"Marca {motocicleta.marca}, Modelo {motocicleta.modelo}, {motocicleta.nro_ruedas} ruedas, Tipo: {motocicleta.tipo}, Motor: {motocicleta.motor}, Cuadro: {motocicleta.cuadro}, Nro Radios: {motocicleta.nro_radios}")

# Verificación de las relaciones de herencia
print(f"\nMotocicleta es instancia de Vehiculo: {isinstance(motocicleta, Vehiculo)}") 
print(f"Motocicleta es instancia de Automovil: {isinstance(motocicleta, Automovil)}") 
print(f"Motocicleta es instancia de Particular: {isinstance(motocicleta, Particular)}") 
print(f"Motocicleta es instancia de Carga: {isinstance(motocicleta, Carga)}") 
print(f"Motocicleta es instancia de Bicicleta: {isinstance(motocicleta, Bicicleta)}") 
print(f"Motocicleta es instancia de Motocicleta: {isinstance(motocicleta, Motocicleta)}")