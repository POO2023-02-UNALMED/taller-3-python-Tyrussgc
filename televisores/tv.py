class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._estado = estado
        self._volumen = 1
        self._control = None
        TV._numTV += 1

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def set_canal(self, canal):
        if self.estado and 1 <= canal <= 120:
            self.canal = canal

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_volumen(self):
        return self.volumen

    def set_volumen(self, volumen):
        if self.estado and 0 <= volumen <= 7:
            self.volumen = volumen

    def get_control(self):
        return self.control

    def set_control(self, control):
        self.control = control

    @staticmethod
    def get_num_TV():
        return TV.numTV

    @staticmethod
    def set_num_TV(nuevo_num_TV):
        TV.numTV = nuevo_num_TV

    def turn_on(self):
        self.estado = True

    def turn_off(self):
        self.estado = False

    def get_estado(self):
        return self.estado

    def canal_up(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canal_down(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumen_up(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumen_down(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1