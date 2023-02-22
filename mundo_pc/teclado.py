from mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado (DispositivoEntrada):  # Teclado hereda de DispositivoEntrada

    contador_teclados = 0

    def __init__(self, marca, tipo_entrada): #recibe los valores de marca y tipo_entrada
        Teclado.contador_teclados +=1 #incrementados en 1 la variable contador_teclados
        self._id_teclado = Teclado.contador_teclados #le asignamos el valor de contador a id
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return f'ID: {self._id_teclado}, Marca: {self._marca}, Tipo de Entrada: {self.tipo_entrada}' #podemos acceder a los atributos por medio de super que llama a la clase padre
    


if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    print(teclado1)
    teclado2 = Teclado('Gamer', 'BlueTooth')
    print(teclado2)
