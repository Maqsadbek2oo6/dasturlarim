class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
    def tanishtir(self):
        print(f"Ismim: {self.ism}\nYoshim: {self.yosh} da")
    def get_age(self):
        print(self.yosh)

class Xodim(Shaxs):
    def __init__(self, ism, familiya, yosh, vazifa):
        super().__init__(ism, yosh)
        self.familiya = familiya
        self.vazifa = vazifa
    def tanishtir(self):
        print(f"Men: {self.ism} {self.familiya}, shu offisda {self.vazifa} lavozimida ishlayman")

class Oquvchi(Shaxs):
    def __init__(self, ism, familiya, yosh, sinf, maktab):
        super().__init__(ism, yosh)
        self.familiya = familiya
        self.sinf = sinf
        self.maktab = maktab
    def tanishtir(self):
        print(f"Ism: {self.ism}\nFamiliya: {self.familiya}\nMaktab: {self.maktab}\nSinf: {self.sinf}")
