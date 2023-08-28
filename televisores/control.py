class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def turnOn(self):
        if self.tv is not None:
            self.tv.turn_on()

    def turnOff(self):
        if self.tv is not None:
            self.tv.turn_off()

    def canalUp(self):
        if self.tv is not None:
            self.tv.canal_Up()

    def canalDown(self):
        if self.tv is not None:
            self.tv.canal_Down()

    def volumenUp(self):
        if self.tv is not None:
            self.tv.volumen_Up()

    def volumenDown(self):
        if self.tv is not None:
            self.tv.volumen_Down()

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def setVolumen(self, volumen):
        if self.tv is not None:
            self.tv.setvolumen(volumen)

    def setCanal(self, canal):
        if self.tv is not None:
            self.tv.setCanal(canal)