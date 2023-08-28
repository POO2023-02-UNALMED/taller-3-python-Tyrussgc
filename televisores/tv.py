class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self.estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getVolumen(self):
        return self.volumen

    def setVolumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def getControl(self):
        return self.control

    def setControl(self, control):
        self.control = control

    @staticmethod
    def getNumTV():
        return TV.numTV

    @staticmethod
    def setNumTV(nuevo_num_TV):
        TV.numTV = nuevo_num_TV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1