class Proprietar:
    def __init__(self, nume, prenume, numar_de_telefon):
        self.__nume = nume
        self.__prenume = prenume
        self.__numar_de_telefon = numar_de_telefon
        self.data_nastere = None
        self.email = None
        self.adresa = None

    def actualizeaza_informatii_proprietar(self, data_nastere, email, adresa):
        self.data_nastere = data_nastere
        self.email = email
        self.adresa = adresa

    def suna_la_cabinet(self):
        # Implementarea pentru a suna la cabinet
        pass

    def programeaza_animalul(self):
        # Implementarea pentru a programa animalul
        pass

    def plateste_factura(self):
        # Implementarea pentru a plăti factura
        pass

    # Getter, setter și deleter pentru atributul nume
    def get_nume(self):
        return self.__nume

    def set_nume(self, nume):
        self.__nume = nume

    def del_nume(self):
        del self.__nume

    # Getter, setter și deleter pentru atributul prenume
    def get_prenume(self):
        return self.__prenume

    def set_prenume(self, prenume):
        self.__prenume = prenume

    def del_prenume(self):
        del self.__prenume

    # Getter, setter și deleter pentru atributul numar_de_telefon
    def get_numar_de_telefon(self):
        return self.__numar_de_telefon

    def set_numar_de_telefon(self, numar_de_telefon):
        self.__numar_de_telefon = numar_de_telefon

    def del_numar_de_telefon(self):
        del self.__numar_de_telefon

# Exemplu de utilizare:
proprietar1 = Proprietar("Popescu", "Ana", "0712345678")
proprietar1.actualizeaza_informatii_proprietar("01-01-1990", "ana.popescu@example.com", "Str. Independentei, nr. 10")

print(proprietar1.get_nume())  # Output: Popescu
print(proprietar1.get_prenume())  # Output: Ana
print(proprietar1.get_numar_de_telefon())  # Output: 0712345678

proprietar1.set_nume("Ionescu")
print(proprietar1.get_nume())  # Output: Ionescu

del proprietar1.nume
# Error: AttributeError: 'Proprietar' object has no attribute 'nume'