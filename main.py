#1
response = [
    {
        "nome": "Loja Exemplo 1",
        "endereço": {
            "rua": "Rua Exemplo 1",
            "cidade": "Exemplo City 1"
        },
        "produtos": [
            {"id": 1, "nome": "Produto A", "preço": 29.99},
            {"id": 2, "nome": "Produto B", "preço": 34.99}
        ]
    },
    {
        "nome": "Loja Exemplo 2",
        "endereço": {
            "rua": "Rua Exemplo 2",
            "cidade": "Exemplo City 2"
        },
        "produtos": [
            {"id": 1, "nome": "Produto C", "preço": 45.50},
            {"id": 2, "nome": "Produto D", "preço": 15.00}
        ]
    },
    {
        "nome": "Loja Exemplo 3",
        "endereço": {
            "rua": "Rua Exemplo 3",
            "cidade": "Exemplo City 3"
        },
        "produtos": [
            {"id": 1, "nome": "Produto E", "preço": 22.00},
            {"id": 2, "nome": "Produto F", "preço": 39.99}
        ]
    },
    {
        "nome": "Loja Exemplo 4",
        "endereço": {
            "rua": "Rua Exemplo 4",
            "cidade": "Exemplo City 4"
        },
        "produtos": [
            {"id": 1, "nome": "Produto G", "preço": 55.00},
            {"id": 2, "nome": "Produto H", "preço": 5.99}
        ]
    },
    {
        "nome": "Loja Exemplo 5",
        "endereço": {
            "rua": "Rua Exemplo 5",
            "cidade": "Exemplo City 5"
        },
        "produtos": [
            {"id": 1, "nome": "Produto I", "preço": 33.00},
            {"id": 2, "nome": "Produto J", "preço": 27.50}
        ]
    }
]

for i in response:
    nova_lista = []
    for j in i["produtos"]:
        if j["preço"] < 30:
            nova_lista.append(j)
    i["produtos"] = nova_lista


#Utilizei essa solução por que é mais prática, fiz iteração nos itens do json, verifiquei os produtos menores que 30 reais e criei uma nova lista


#2

responsejson = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}

produto_b = responsejson["produtos"][1]["preço"]
print(produto_b)

# Fui diretamente no item dele, entrei em produtos e depois no produto B de indice[1] e depois no "preço"

#3
lista = [5,8,3,0,8,1,9,10,20,30]
lista.sort()

# Sort é o metodo mais convencional pra ordenar uma lista de números

#4 
lista = ["   joao   ","   maria   ","  joana  "]
lista_correta = []
for i in lista:
    nomes = i.split()
    lista_correta.append(nomes)

print(lista_correta)

# Split é o metodo usado pra tirar espaçamento das strings, por isso o usei

#5

lista = [1,2,3,4,5,6,9]
numero_retirado = lista.pop(1)
print(numero_retirado)

# O segundo item tem índice [1] usei o método pop() para tira-lo


#6
lista = ["joao", "ana", "joana","joao", "ricardo", "joao"]
for i in range(len(lista)):
    if lista[i] =="joao":
        lista[i] ="maria"

print(lista)

# Eu usaria replace mas so funciona diretamente em strings e nao em listas, entao fiz a iteracao e uma estrutura condicional

#7

var = 0
lista = [1,2,3,4,5,6,7,8,9,10]
while var <=5:
    print(lista[var])
    var+=1

# Usei o while pra iterar na lista, e ele so printa ate o numero 6, pois quando var chega em 5 o loop quebra

#8
import requests
def requisicao_tasks():
    requisicao = requests.get('https://jsonplaceholder.typicode.com/todos')

    if requisicao.status_code == 200:
        tarefas = requisicao.json()

        completas = 0
        pendentes = 0

        for i in tarefas:
            if i["completed"]:
                completas+=1
            else:
                pendentes+=1
        return completas,pendentes
    else:
        return "Erro"


completas,pendentes = requisicao_tasks()
print(f'completas: {completas}')
print(f'pendentes: {pendentes}')

# usei o request get pra pegar a api, depois vi se o status code é 200 pra ver se a solicitacao foi bem sucedida, criei variaveis pra completas e pendentes e vi se dentro das tasks quais estavam completas e pendentes

#9
import requests
def requisicao_dados():
    requisicao = requests.get('https://jsonplaceholder.typicode.com/users')
    if requisicao.status_code == 200:
        listas = requisicao.json()
        dados = []
        for i in listas:
            nome = i["name"]
            username = i["username"]
            email = i["email"]
            rua = i["address"]["street"]
            numero = i["address"]["suite"]

            dados_requeridos = {
                "Nome":nome,
                "Username":username,
                "Email":email,
                "Rua":rua,
                "Numero":numero
            }

            dados.append(dados_requeridos)
        return dados
    else:
         return "Erro"


user = requisicao_dados()
print(user)

# Aqui eu usei o get pra pegar a api, criei uma nova lista, iterei sobre as listas do json, salvei variaveis dos itens que eu queria e depois usei append na lista vazia que eu tinha criado

#10

lista = []

lista.append('Mohamed')
lista.append('Smaili')

print(lista)

lista.pop(0)
print(lista)

# O primeiro item que adiciono é o primeiro a ser removido, adicionei meu nome proimeiro depois o sobrenome, e depois removi o primeiro indice, e so fico umeu sobrenome

#11

lista = []

for i in range(1,10):
    lista.append(i)

print(lista)
while lista:
    numero_removido = lista.pop()
    print(numero_removido)

# O ultimo item que entra é o primeiro que sai, criei um while e dentro dele uma variavel que vai tirando numero por numero, do ultimo ao primeiro

















    


















