class ClinicaVeterinara:
    def __init__(self, nume, adresa, nr_telefon, data_infiintare, cont_bancar):
        self._nume = nume
        self._adresa = adresa
        self._nr_telefon = nr_telefon
        self.data_infiintare = data_infiintare
        self.cont_bancar = cont_bancar
        self.vizite_animal = []

    def consulta_animal(self, animal):
        # Implementarea pentru consultația animalului
        pass

    def calculeaza_factura(self, servicii):
        # Implementarea pentru calcularea facturii
        pass

    def realimenteaza_stoc_medicamente(self, medicamente):
        # Implementarea pentru realimentarea stocului de medicamente
        pass

# Exemplu de utilizare
clinica = ClinicaVeterinara("Clinica Veterinara Dr. Pet", "Str. Principala nr. 10", "0722333444", "01-01-2000", "ROXX123456789")
print(clinica._nume)  # Output: Clinica Veterinara Dr. Pet
print(clinica._adresa)  # Output: Str. Principala nr. 10
print(clinica._nr_telefon)  # Output: 0722333444

clinica._nume = "Noul Nume"
print(clinica._nume)  # Output: Noul Nume