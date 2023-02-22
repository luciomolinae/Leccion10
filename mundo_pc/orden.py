class Orden:

    contador_ordenes = 0

    def __init__(self, computadoras):
        Orden.contador_ordenes += 1
        self._id_orden = Orden.contador_ordenes
        self._computadoras = computadoras

    def agregar_computadora(self, computadora): #anexa un objeto de tipo computadora a nuestra lista
        self._computadoras.append(computadora)

    def __str__(self):
        computadoras_str = '' #almacena todos los objetos de tipo computadora
        for computadora in self._computadoras:
            computadoras_str += computadora.__str__() #agrega a la variable temporal cada una de las llamadas al metodo str de cada objeto computadora que tengamos en la lista


        return f'''
                Orden: {self._id_orden}
                Computadoras: {computadoras_str} 
        '''
        # contiene todas las llamadas str a cada objeto de tipo computadora