from src.models.Usuario import Usuario 
from src.models.Adotante import Adotante 
from src.models.Doador import Doador 
from src.models.Pet import Pet 

# Adotantes
adotante1 = Adotante("Lucas", "01/01/2000", "Rua A, 123", "123456789", "00000000000", "12345678901")
adotante2 = Adotante("Ana", "02/02/1995", "Rua B, 456", "987654321", "00000000000", "12345678901")

#  Doadores
doador1 = Doador("Carlos", "03/03/1985", "Rua C, 789", "456789123", "00000000000", "12345678901")
doador2 = Doador("Maria", "04/04/1990", "Rua D, 101", "321654987", "00000000000", "12345678901")






pet1=Pet("Rex", 2, "Feliz", "Labrador", "Macho", True, True)
pet2=Pet("Mia", 3, "Triste", "Siamês", "Fêmea", True, False)




print("    *******      Adotantes      *******    ")
print(adotante1.getInfo(),'\n')
print(adotante2.getInfo(),'\n')

print("    *******      Doadores      *******    ")
print(doador1.getInfo(),'\n')
print(doador2.getInfo(),'\n')


print("    *******      Pets      *******    ")
print(pet1.getInfo(),'\n')
print(pet2.getInfo(),'\n')
