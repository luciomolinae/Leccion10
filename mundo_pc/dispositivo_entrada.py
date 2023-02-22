class DispositivoEntrada:
    def __init__(self, marca, tipo_entrada):
        self._marca = marca
        self._tipo_entrada = tipo_entrada

    def __str__(self):
        return f'Marca {self._marca}, Entrada: {self._tipo_entrada}'

    @property  # Decorador que permite acceder al atributo
    def marca(self):
        # print('Llamando al metodo get nombre')
        return self._marca

    @marca.setter
    def marca(self, marca):
        # print('Llamando al metodo set nombre')
        self._marca = marca

    @property
    def tipo_entrada(self):
        return self._tipo_entrada

    @tipo_entrada.setter
    def tipo_entrada(self, tipo_entrada):
        return self._tipo_entrada