class Animal(object):
    def __init__(self, nume, data_nastere, rasa, specie, proprietar):
        self.nume = nume
        self.data_nastere = data_nastere
        self.rasa = rasa
        self.specie = specie
        self.proprietar = proprietar

    def somn(self):
        raise NotImplementedError("Metoda somn() trebuie implementată în subclasă.")

    def sunet(self):
        raise NotImplementedError("Metoda sunet() trebuie implementată în subclasă.")

    def activitati(self):
        raise NotImplementedError("Metoda activitati() trebuie implementată în subclasă.")

# Exemplu de clasă care implementează clasa Animal
class Pisica(Animal):
    def somn(self):
        return "{} doarme.".format(self.nume)

    def sunet(self):
        return "{} face miau.".format(self.nume)

    def activitati(self):
        return "{} se joacă cu o minge.".format(self.nume)

# Exemplu de utilizare
proprietar_pisica = "Ana"
pisica1 = Pisica("Tom", "01-01-2018", "birmanez", "pisica", proprietar_pisica)

print(pisica1.somn())  # Output: Tom doarme.
print(pisica1.sunet())  # Output: Tom face miau.
print(pisica1.activitati())  # Output: Tom se joacă cu o minge.