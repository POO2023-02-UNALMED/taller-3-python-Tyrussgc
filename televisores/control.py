class Control:
    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self.tv = tv
        tv.setControl(self)

    def turnOn(self):
        if self.tv is not None:
            self.tv.turnOn()

    def turnOff(self):
        if self.tv is not None:
            self.tv.turnOff()

    def canalUp(self):
        if self.tv is not None:
            self.tv.canalUp()

    def canalDown(self):
        if self.tv is not None:
            self.tv.canalDown()

    def volumenUp(self):
        if self.tv is not None:
            self.tv.volumenUp()

    def volumenDown(self):
        if self.tv is not None:
            self.tv.volumenDown()

    def getTv(self):
        return self.tv

    def setTv(self, tv):
        self.tv = tv

    def setVolumen(self, volumen):
        if self.tv is not None:
            self.tv.setVolumen(volumen)

    def setCanal(self, canal):
        if self.tv is not None:
            self.tv.setCanal(canal)