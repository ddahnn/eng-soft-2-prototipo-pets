from src.builders.PetBuilder import PetBuilder
from src.factories.UserFac import UserFac


adotante1 = UserFac.criar_usuario(
    tipo="Adotante",
    nome="Carla Souza",
    endereco="Rua das Flores, 123",
    telefone="(11) 91234-5678",
    cpf="123.456.789-00"
)

adotante2 = UserFac.criar_usuario(
    tipo="Adotante",
    nome="Felipe Rocha",
    endereco="Av. Paulista, 456",
    telefone="(11) 98888-9999",
    cpf="321.654.987-00"
)

adotante3 = UserFac.criar_usuario(
    tipo="Adotante",
    nome="Juliana Lima",
    endereco="Rua das Palmeiras, 789",
    telefone="(21) 97777-8888",
    cpf="456.123.789-00"
)



vendedor1 = UserFac.criar_usuario(
    tipo="Vendedor",
    nome="PetShop Animal Feliz",
    endereco="Av. Pet, 1000",
    telefone="(11) 90000-1111",
    cnpj="00.000.000/0001-00"
)

vendedor2 = UserFac.criar_usuario(
    tipo="Vendedor",
    nome="Cantinho Pet",
    endereco="Rua Pet Lovers, 555",
    telefone="(21) 95555-4444",
    cnpj="11.111.111/0001-11"
)

vendedor3 = UserFac.criar_usuario(
    tipo="Vendedor",
    nome="Loja Pet Amigo",
    endereco="Rua das Rosas, 77",
    telefone="(31) 96666-3333",
    cnpj="22.222.222/0001-22"
)



anjo1 = UserFac.criar_usuario(
    tipo="Resgatador",
    nome="Marcos Nunes",
    endereco="Rua do Amor, 22",
    telefone="(11) 93333-2222",
    rg="MG-12.345.678",
    cpf="789.456.123-00"
)

anjo2 = UserFac.criar_usuario(
    tipo="Anjo",
    nome="Beatriz Silva",
    endereco="Rua dos Pets, 88",
    telefone="(21) 94444-1111",
    rg="RJ-98.765.432",
    cpf="654.987.321-00"
)

anjo3 = UserFac.criar_usuario(
    tipo="Resgatador",
    nome="Joana Prado",
    endereco="Av. Felicidade, 505",
    telefone="(31) 97777-6666",
    rg="MG-11.111.111",
    cpf="321.321.321-00"
)



admin1 = UserFac.criar_usuario(
    tipo="Admin",
    nome="Carlos Admin",
    endereco="Centro Adm, 10",
    telefone="(11) 91111-1111",
    email_admin="admin1@pethub.com"
)

admin2 = UserFac.criar_usuario(
    tipo="Admin",
    nome="Luciana Gestora",
    endereco="Av. Central, 20",
    telefone="(21) 92222-2222",
    email_admin="admin2@pethub.com"
)

admin3 = UserFac.criar_usuario(
    tipo="Admin",
    nome="Rafael Supervisor",
    endereco="Rua da Justiça, 30",
    telefone="(31) 93333-3333",
    email_admin="admin3@pethub.com"
)



pet = (
    PetBuilder()
    .set_nome("Rex")
    .set_especie("Cachorro")
    .set_idade(3)
    .set_sexo("Macho")
    .set_localizacao("São Paulo - SP")
    .set_fotos(["foto1.jpg", "foto2.jpg", "foto3.jpg"])
    .set_raca("SRD")
    .set_castracao(True)
    .set_temperamento("Brincalhão e dócil")
    .build()
)

print(adotante1.informacoes())
print(vendedor1.informacoes())
print(anjo1.informacoes())
print(admin1.informacoes())
print(pet)
