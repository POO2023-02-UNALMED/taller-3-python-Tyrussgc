class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.set_control(self)

    def turnOn(self):
        if self.tv is not None:
            self.tv.turn_on()

    def turnOff(self):
        if self.tv is not None:
            self.tv.turn_off()

    def canalUp(self):
        if self.tv is not None:
            self.tv.canal_up()

    def canalDown(self):
        if self.tv is not None:
            self.tv.canal_down()

    def volumenUp(self):
        if self.tv is not None:
            self.tv.volumen_up()

    def volumenDown(self):
        if self.tv is not None:
            self.tv.volumen_down()

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def setVolumen(self, volumen):
        if self.tv is not None:
            self.tv.set_volumen(volumen)

    def setCanal(self, canal):
        if self.tv is not None:
            self.tv.set_canal(canal)