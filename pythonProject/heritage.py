class Batiment:
    def __init__(self, adresse, nb_etages):
        self.adresse = adresse
        self.nb_etages = nb_etages

    def get_adresse(self):
        return self.adresse

    def get_nb_etages(self):
        return self.nb_etges

class Immeuble(Batiment):
    def __init__(self, adresse, nb_etages, nb_balcons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_balcons = nb_balcons

    def get_nb_balcons(self):
        return self.nb_balcons

class Supermarche(Batiment):

    def __init__(self, adresse, nb_etages, nb_rayons):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_rayons = nb_rayons

    def get_nb_rayons(self):
        return self.nb_rayons

class Banque(Batiment):

    def __init__(self, adresse, nb_etages, nb_coffres, nom):
        Batiment.__init__(self, adresse, nb_etages)
        self.nb_coffres = nb_coffres
        self.nom = nom

    def get_nb_coffres(self):
        return self.nb_coffres

    def get_nom(self):
        return self.nom


Immeuble1 = Immeuble("503 Rue Merkel", 3,3)
Immeuble2 = Immeuble("503 Rue Merkel", 3,7)
Immeuble3 = Immeuble("503 Rue Nanhas",1 ,3)
Immeuble4 = Immeuble("503 Rue Nanhas", 7,2)
Immeuble5 = Immeuble("503 Rue de la joie", 12,24)

supermarche1 = Supermarche("209 rue nas", 1, 34)
supermarche1 = Supermarche("209 rue tech4tchad", 3, 12)

banque = Banque("10 boulevard SAO", 43,"NasBanque")


