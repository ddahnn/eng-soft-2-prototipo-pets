from src.models.Usuario import Usuario 
from src.models.Adotante import Adotante 
from src.models.Doador import Doador 
from src.models.Pet import Pet 
from src.builders.PetBuilder import PetBuilder


# Adotantes
adotante1 = Adotante("Lucas", "01/01/2000", "Rua A, 123", "123456789", "00000000000", "12345678901")
adotante2 = Adotante("Ana", "02/02/1995", "Rua B, 456", "987654321", "00000000000", "12345678901")


#  Doadores
doador1 = Doador("Carlos", "03/03/1985", "Rua C, 789", "456789123", "00000000000", "12345678901")
doador2 = Doador("Maria", "04/04/1990", "Rua D, 101", "321654987", "00000000000", "12345678901")



# Pet
pet1=Pet("Rex", 5, "Cachorro", "Macho", False)
pet2=Pet("Mia", 3, "Gato", "Fêmea", True)   
pet3=Pet("Luna", 2, "Coelho", "Fêmea", False)


# Adicionando vacinas
pet1.adicionar_vacinas("Raiva")
pet1.adicionar_vacinas("V8")
pet3.adicionar_vacinas("prevenção")
pet2.adicionar_vacinas("Parva")


# Verificando lista de vacinas
pet1.ver_lista_Vacinas()
pet2.ver_lista_Vacinas()
pet3.ver_lista_Vacinas()




print("    *******      Adotantes      *******    ")
print(adotante1.getInfo(),'\n')
print(adotante2.getInfo(),'\n')

print("    *******      Doadores      *******    ")
print(doador1.getInfo(),'\n')
print(doador2.getInfo(),'\n')


print("    *******      Pets      *******    ")
print(pet1.getInfo(),'\n')
print(pet2.getInfo(),'\n')




print("    *******      Builder Pet      *******    ")
builder = PetBuilder()
pet = (builder
       .set_nome("Rex")
       .set_idade(3)
       .set_especie("Cachorro")
       .set_sexo("Macho")
       .set_castrado(True)
       .adicionar_vacina("Antirrábica")
       .build())

print(pet.getInfo())
