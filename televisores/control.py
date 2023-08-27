class Control:
    def __init__(self):
        self._tv = None

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