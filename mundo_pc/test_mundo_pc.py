from mundo_pc.computadora import Computadora
from mundo_pc.monitor import Monitor
from mundo_pc.orden import Orden
from mundo_pc.raton import Raton
from mundo_pc.teclado import Teclado

monitor1 = Monitor('HP', 15)
raton1 = Raton('HP', 'USB')
teclado1 = Teclado('HP', 'USB')
computadora1 = Computadora('HP', monitor1, teclado1, raton1) #referencias de los objetos

teclado2 = Teclado('Acer', 'Bluetooth')
raton2 = Raton('Acer', 'Bluetooth')
monitor2 = Monitor('Acer', 27)
computadora2 = Computadora('Acer', monitor2, teclado2, raton2)

teclado3 = Teclado('Gamer', 'Bluetooth')
raton3 = Raton('Gamer', 'Bluetooth')
monitor3 = Monitor('Gamer', 34)
computadora3 = Computadora('Gamer', monitor3, teclado3, raton3)

computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1) #le pasamos el listado de tipo computadora
orden1.agregar_computadora(computadora3) #agrega el objeto computadora3 a la lista de la orden1
print(orden1)

computadoras2 = [computadora2, computadora3]
orden2 = Orden(computadoras2)
print(orden2)
