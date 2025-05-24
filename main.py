from src.models.Pet import Pet


pet1 = Pet("Rex", 5, "Labrador", "Cachorro", "Grande", 30, "Preto", "Macho", "São Paulo")
pet2 = Pet("Mia", 3, "Siamês", "Gato", "Pequeno", 5, "Branco", "Fêmea", "Rio de Janeiro")

print(pet1.getInformacoes())
print(pet2.getInformacoes())