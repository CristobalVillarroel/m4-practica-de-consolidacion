from dataclasses import dataclass

@dataclass
class Vehiculo:
    marca:str
    modelo:str
    nro_ruedas:int

@dataclass
class Automovil(Vehiculo):
    velocidad:int
    cilindrada:int

@dataclass
class Particular(Automovil):
    nro_puestos:int

@dataclass
class Carga(Automovil):
    peso_carga:int

@dataclass
class Bicicleta(Vehiculo):
    tipo:str

@dataclass
class Motocicleta(Bicicleta):
    motor:int
    cuadro:str
    nro_radios:str