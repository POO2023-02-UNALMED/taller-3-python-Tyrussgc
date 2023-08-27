class Marca:
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

class TV:
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.canal = 1
        self.precio = 500
        self.estado = estado
        self.volumen = 1
        self.control = None
        TV.numTV += 1

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


class Control:
    def __init__(self):
        self.tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.set_control(self)

    def turn_on(self):
        if self.tv is not None:
            self.tv.turn_on()

    def turn_off(self):
        if self.tv is not None:
            self.tv.turn_off()

    def canal_up(self):
        if self.tv is not None:
            self.tv.canal_up()

    def canal_down(self):
        if self.tv is not None:
            self.tv.canal_down()

    def volumen_up(self):
        if self.tv is not None:
            self.tv.volumen_up()

    def volumen_down(self):
        if self.tv is not None:
            self.tv.volumen_down()

    def get_tv(self):
        return self.tv

    def set_tv(self, tv):
        self.tv = tv

    def set_volumen(self, volumen):
        if self.tv is not None:
            self.tv.set_volumen(volumen)

    def set_canal(self, canal):
        if self.tv is not None:
            self.tv.set_canal(canal)