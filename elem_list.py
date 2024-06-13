# Lista de tuplas, onde cada tupla contém um nome, altura e peso
lista_de_tuplas = [('Pedro', 1.74, 81), ('Júlia', 1.65, 67), ('Otávio', 1.81, 83)]

# Inicializa uma lista vazia para armazenar os pesos
lista = []

# Itera sobre cada tupla em lista_de_tuplas
for tupla in lista_de_tuplas:
    # Adiciona o terceiro elemento (peso) da tupla à lista
    lista.append(tupla[2])

# Imprime a lista contendo apenas os pesos
print(lista)
