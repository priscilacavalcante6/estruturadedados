#Criação de uma lista

frutas = ["maçã","banana","cereja","laranja"]

#Adicionando elementos
frutas.append("kiwi") #Adiciona ao final
frutas.insert(1, "manga") #Insere na posição 1


#Removendo Elementos

frutas.remove("banana") #Remove pelo valor
del frutas[0] #Remove pelo indíce
frutas.pop() #Remove e retorna o ultimo elemento

#Acessando elementos
print(frutas[2]) #Acesse o terceiro elemento
print(frutas[-1]) #Acesse o último elemento


#Modificando Elementos

frutas[1] = "abacate" # Modifica o elemento na posição 1

#Verificando a existência de um elemento
if "abacate" in frutas:
    print("Abacate está na lista")

print(frutas)

#Criação de uma Lista: a lista a seguir armazena uma sequência de números inteiros.

lista_numerica = [1, 2, 3, 4, 5] 
print(lista_numerica)

#Heterogeneidade dos elementos: esta lista contém uma combinação de strings, números de ponto flutuante, inteiros e valores booleanos.

lista_mista = ["Python", 3.7, 2023, False]
print(lista_mista)

#Acesso a elementos: acessar o elemento na primeira posição, que retorna o valor 1.

primeiro_elemento = lista_numerica[0]
print(primeiro_elemento)

#Alteração de elementos: modificar um item específico, resultando na alteração do segundo elemento para 10.

lista_numerica[1] = 10
print(lista_numerica) 

#Inserção de elementos: utilizando o método a seguir, adiciona o número 6 ao final da lista.

lista_numerica.append(6)
print(lista_numerica)

#Remoção de elementos: o comando a seguir exclui o número 3 da lista.

lista_numerica.remove(3)
print(lista_numerica)

#Determinação do tamanho da lista: fornece o número total de elementos na lista.

len(lista_numerica)
print(lista_numerica)

#Listas aninhadas: criação de listas dentro de listas.

lista_aninhada = [[1, 2], [3, 4, 5]]
print(lista_aninhada)

# Exemplos de tuplas:

# Criação com parênteses: aqui, minha_tupla é uma tupla contendo três números inteiros.

minha_tupla = (1, 2, 3)
print(minha_tupla)

# Criação sem parênteses: esta também é uma tupla válida, contendo três números.

outra_tupla = 4, 5, 6
print(outra_tupla)

# Dicionários em Python, conhecidos como dict, são estruturas de dados que armazenam pares de chave-valor. 
# Eles são coleções não ordenadas, mas são mutáveis, permitindo que os dados sejam modificados após a criação. 
# Cada chave no dicionário é única e é usada para acessar o valor correspondente. 
# Dicionários são ideais para casos em que as relações entre os dados são essenciais (Alves, 2021).

# Considere o seguinte exemplo acadêmico:

dicionario_curso = {"nome": "Ciência da Computação", "créditos": 240}
print(dicionario_curso)



# Criando um dicionário

info_estudante = {
    'nome': 'Ana Silva',
    'idade': 22,
    'curso': 'Engenharia de Software'
}

# Exibir as chaves e valores corretamente
print(f"Chaves: {info_estudante.keys()}")
print(f"Valores: {info_estudante.values()}")

# Acessando as chaves do dicionário

chaves = info_estudante.keys()

print("Chaves:", chaves) # Saída: Chaves: dict_keys(['nome', 'idade', 'curso'])

# Acessando os valores do dicionário

valores = info_estudante.values()

print("Valores:", valores) # Saída: Valores: dict_values(['Ana Silva', 22, 'Engenharia de Software'])

# Conjuntos
# Conjuntos em Python, conhecidos como set, são coleções que armazenam elementos únicos e não ordenados. 
# Diferente das listas e tuplas, os conjuntos não permitem valores duplicados, e a ordem dos elementos não é garantida. 
# Eles são particularmente úteis para operações como união, interseção e diferença, comuns em lógica de conjuntos matemáticos.
# Criação de um conjunto:

meu_conjunto = {1, 2, 3, 4, 5}
print(meu_conjunto)

# Aqui, meu_conjunto é um conjunto com números inteiros de 1 a 5

# Adicionando elementos:
meu_conjunto.add(6)
print(meu_conjunto)

# Isso adiciona o número 6 ao conjunto, caso ele ainda não esteja presente.

# Removendo elementos:

meu_conjunto.remove(2)
print(meu_conjunto)


# Operações de conjunto: assim como as operações matemáticas, podemos realizar operações como a união, 
# interseção, etc.

# União:
conjunto_a = {1, 2, 3} 

conjunto_b = {3, 4, 5} 

uniao = conjunto_a.union(conjunto_b) 

print(uniao) # Saída: {1, 2, 3, 4, 5}