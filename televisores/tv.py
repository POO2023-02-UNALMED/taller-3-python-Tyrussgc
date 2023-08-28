class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV._numTV += 1

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
        self.marca = marca

    def setCanal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal
    def getCanal(self):
        return self.canal

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
    def get_num_TV():
        return TV._numTV

    def set_num_TV(nuevo_Num_TV):
        TV._numTV = nuevo_Num_TV

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