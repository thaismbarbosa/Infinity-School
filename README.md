Anotações das aulas

# Definindo uma lista de numeros
lista_de_numeros = [1,2,3,4,5]

# Definindo uma lista de letras
lista_de_letras = ['a', 'i', 'u', 'e', 'o']

# Definindo uma lista de valores logicos
lista_de_logicos = [True, False, False, True]

# Lista com diferentes tipos de dados
lista_mista = ['Gabriel', 12, True]

# Lista com as cinco primeiras letras do alfabeto, ultilizando numeros negativos podemos acessar os indices de qualquer lista
letras = ['a', 'b', 'c', 'd','e']
print(letras [-1])

# Adicionando itens ao final da lista com metodo .append()
numeros = [1, 2, 3, 4, 5]
numeros.append(6)
print(numeros)
resultado = [1, 2, 3, 4, 5, 6]

# Adicionando itens ao final da lista com metodo .insert()
numeros = [10, 30, 40, 50]
letras = ['a', 'e', 'o', 'u']
pesos = [1.2, 3.4, 5.3, 6.7]

numeros.insert(1, 20) inserindo 20 na posição 1
letras.insert(2, 'i') inserindo 'i' na posição 2
pesos.insert(2, 4.0) inserindo 4.0 na posição 3

numeros = [10, 20, 30, 40, 50]
letras = ['a', 'e', 'i', 'o', 'u']
pesos = [1.2, 3.4, 4.0, 5.3, 6.7]

# Removendo itens atraves do indice

notas = [
    9.0,  INDICE 0
    8.7,  INDICE 1
    9.9,  INDICE 2
    8.7,  INDICE 3
    7.9   INDICE 4
    ]
notas.pop(0) remove a nota 9.0
notas.pop(1) remove a nota 9.9
notas.pop(2) remove a nota 7.9

print(notas) resultado [8.7, 8.7]

# Removendo itens atraves do valor

finalistas_obmep = [
    "Maria da silva santos",
    "Pedro henrique oliveira",
    "Ana carolina pereira costa",
    "Joao fernandes rodrigues",
    "Laura nunes almeida"
]

finalistas_obmep.remove("Ana carolina pereira costa")
print(finalistas_obmep)

# Iterando listas em Python coom FOR

# Definição da lista de compras

lista_compras = [
    "2 pcts. de Arroz",
    "6 pcts. de Feijão",
    "2 pcts. de farinnha de Mandioca",
    "4kg de linguiça calabresa",
    "4kg de charque",
    "2kg de bacon de barriga",
    "2kg  de pe e orelha de porco",
    "1 pct. de folha de louro",
    "6 moi de couve",
    "5kg de laranja"
]

print("LISTA DE COMPRAS", end='\n\n')

# Percorrendo a lista de compras
for item in lista_compras:
    print("[ ]", item)

# Definindo e exibindo valores de uma tupla e mostrando a diferença entre tupla e lista

# Lista mutável

minha_lista = [1, 2, 3, 4, 5]
minha_lista[0] = 10 #modificando um  elemento
print(minha_lista) #saida: [10, 2, 3, 4, 5]

# Tupla imutável

minha_tupla = (1, 2, 3, 4, 5)
minha_tupla[0] = 10 #Isso resultará em um erro, pois as tuplas sao imutaveis
print(minha_tupla)  #saida: (1, 2, 3, 4, 5)

# Criando uma tupla
frutas = ("maçã", "banana", "laranja", "abacaxi")

# Metodo index(): Retorna o indice do primeiro elemento especificado
indice_laranja = frutas.index("laranja")
print("Indice da laranja: ", indice_laranja)

# Metodo count(): Retorna o numero de ocorrencias de um elemento
quantidade_bananas = frutas.count("banana")
print("Quantidade de bananas: ", quantidade_bananas)

# Desempacotando uma tupla
maca, banana, laranja, abacaxi = frutas
print("Fruta 1: ", maca)
print("Fruta 2: ", banana)
print("Fruta 3: ", laranja)
print("Fruta 4: ", abacaxi)

# Usaando a funcão list() voce pode converter outros tipos de dados iteraveis(como strings, tuplas, conjuntos, etc)

minha_string = "hello"
lista_da_string = list(minha_string)

# Set(conjunto)

set" (conjunto) é uma coleção de elementos
únicos e não ordenados. Isso significa que um
conjunto não permite elementos duplicados e não
mantém a ordem de inserção dos elementos.

Os conjuntos são uma das estruturas de dados
fundamentais da linguagem Python e são úteis para
várias operações matemáticas e tarefas que
envolvem coleções únicas de elementos.

# Exemplos de set e seus usos

meu_set = {'Infinity', 'School'}
print(type(meu_set))
saida <class 'set'>

frutas = {"maçã", "banana", "cereja", "banana"}
print(frutas)
saida {"maçã", "banana", "cereja"}

# Metodo add()

Com esse metodo podemos adicionar uma novo item ao set
pq quando um set é criado nao pode ser alterado,
mas podemos adicionar novos itens.

convidados = {'João', 'Maria', 'Eduarda'}
convidados.add('Marcela')
print(convidados)
saida = {'João', 'Maria', 'Eduarda', 'Marcela'}

# Metodo update()

Usamos esse metodo para adicionar itens de um conjunto ao set especificado
Voce pode utilizar esse metodo com qualquer tipo de objeto
(tuplas, listas, dicionarios, etcs)

ids = {10, 12, 13, 14}
novos_ids = {11, 13, 15}
ids.update(novos_ids)
print(ids)
saida = {10, 11, 12, 13, 14, 15}

# Nao podemos percorrer o set pelo indice

# Metodo remove() e discard()

usamos esse metodo para remover itens de um set

convidados = {'João', 'Maria', 'Eduarda'}
print(convidados.remove('Maria'))
print(convidados.discard('Eduarda'))

saida = {'João'}

# Operações matematicas com set

Os Sets em Python nada mais
são que Conjuntos
Matemáticos. Neles, você
também pode aplicar os
conceitos de Interseção,
União, Diferença e etc.

# Metodo intersection()

O método intersection() retorna um novo conjunto contendo
apenas os itens presentes em ambos:

convidados = {'João', 'Maria', 'Eduarda'}
convidados2 = {'Pedro', 'Maria', 'Raama'}
print(convidados.intersection(convidados2))
saida = {'Maria'}

# Metodo intersection_update()

Se você deseja já atualizar um dos sets com a interseção entre
eles, use o método intersection_update():

convidados = {'João', 'Maria', 'Eduarda'}
convidados2 = {'Pedro', 'Maria', 'Raama'}
print(convidados.intersection_update(convidados2))
saida = {'Maria'}

# Metodo union()

Você pode utilizar o método union()
para retornar um
conjunto de elementos contendo
elemento de ambos sets:

set1 = {1, 2, 3}
set2 = {'z', 'x', 'a'}
print(set1.union(set2)) ou print(set1 | set2)
saida = {1, 2, 3, 'x', 'a', 'z'}
