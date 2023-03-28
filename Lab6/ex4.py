class Celula:
    def get_nume(self):
        raise NotImplementedError("Celula este o interfata")


class FibraMusculara(Celula):
    def __init__(self, nume, masa_musculara):
        self.nume = nume
        self.masa_musculara = masa_musculara

    def get_nume(self):
        return self.nume

    def get_masa_musculara(self):
        return self.masa_musculara


class MuschiGeneric(FibraMusculara):
    def __init__(self, nume, masa_musculara, scop, fibre=[]):
        FibraMusculara.__init__(self, nume, masa_musculara)

        self.scop = scop
        self.fibre = fibre

    def get_scop(self):
        return self.scop


class FibraNervoasa(Celula):
    def __init__(self, nume, lungime):
        self.nume = nume
        self.lungime = lungime

    def get_nume(self):
        return self.nume

    def get_lungime(self):
        return self.lungime


class TrunchiNervos(FibraNervoasa):
    def __init__(self, nume, lungime, specializare, nervi=[]):
        FibraNervoasa.__init__(self, nume, lungime)

        self.specializare = specializare
        self.nervi = nervi

    def get_specializare(self):
        return self.specializare


class Bombardier:
    def __init__(self, nume, bani, muschi):
        self.nume = nume
        self.bani = bani
        self.muschi = muschi
        self.nervi = []

    def mergi_la_sala(self, muschi_antrenat, factor_combinatie=1.5):
        self.muschi.append(muschi_antrenat)

        # cand merge la sala mai face o combinatie
        # si tot iese pe profit
        self.bani = factor_combinatie * self.bani

    def get_masa_musculara(self):
        masa_musculara = 0

        for m in self.muschi:
            masa_musculara += m.get_masa_musculara()

        return masa_musculara

    def muschii_cu_scop(self, scop="forta"):
        return filter(lambda m: m.get_scop() == scop, self.muschi)


if __name__ == "__main__":
    biceps = MuschiGeneric(
        "Biceps",
        50,
        "forta",
        [
            FibraMusculara("Bucata1_Biceps", 25),
            FibraMusculara("Bucata2_Biceps", 25),
        ],
    )

    triceps = MuschiGeneric(
        "Triceps",
        30,
        "smecherie",
        [
            FibraMusculara("Bucata1_Triceps", 15),
            FibraMusculara("Bucata2_Triceps", 15),
        ],
    )

    gelu = Bombardier(
        "Gelu Fura-Vitelu",
        # vrea sa stranga 7000e pt bmv 2003
        5000,
        [biceps, triceps],
    )

    print(
        gelu.nume
        + " are "
        + str(gelu.bani)
        + "euro, vrea sa stranga 7000e pt bmv 2003 asa ca merge la sala sa faca o combinatie"
    )

    print("a inceput cu atatea kg de muschi: " + str(gelu.get_masa_musculara()))
    print()

    gelu.mergi_la_sala(
        MuschiGeneric(
            "Piept",
            80,
            "forta",
            [
                FibraMusculara("Bucata1_Piept", 20),
                FibraMusculara("Bucata2_Piept", 20),
                FibraMusculara("Bucata3_Piept", 20),
                FibraMusculara("Bucata4_Piept", 20),
            ],
        )
    )

    print(
        gelu.nume
        + " are "
        + str(gelu.bani)
        + "euro, a reusit sa stanga bani pt un bmv 2003"
    )

    print("a ajuns cu atatea kg de muschi: " + str(gelu.get_masa_musculara()))
    print()
