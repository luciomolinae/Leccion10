from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):

    contador_ratones = 0

    def __init__(self, marca, tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton= Raton.contador_ratones
        super().__init__(marca, tipo_entrada) # Inicializa los atributos heredados de la clase padre

    def __str__(self): #representa al objeto Raton
        return  f'ID: {self._id_raton}, Marca:{self._marca}, Tipo de Entrada: {self._tipo_entrada}'



if __name__ == '__main__':  # comprobamos si se ejecuta desde este mismop archivo, si es correcto, el codigo esta bien
    raton1 = Raton('HP', 'USB') #Creamos un objeto de la clase Raton
    print(raton1) # Llama al metodo str de una
    raton2 = Raton('Acer', 'Bluetooth')
    print(raton2)