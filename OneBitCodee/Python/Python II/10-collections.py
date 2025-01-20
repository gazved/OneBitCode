import collections
from operator import itemgetter
from collections import deque

#contar itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Uva","Maçã", "Uva", "Banana"]

print(collections.Counter(fruits))

#utilizar tupla nomeada
game = collections.namedtuple('game', ['name', 'preco', 'nota'])
g1 = game("Fifa 23", 90.50, 8.5)


# 3 - Ordenando dicionários
studants = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
a = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(a)
#a biblioteca não é necessaria para ordenar, pode-se usar lambda
students = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}
a = sorted(students.items(), key=lambda x: x[0])  # x[0] é a chave
print(a)


#ordenar pelo valor :
a = sorted(students.items(), key=lambda x: x[1])  # x[1] é o valor
print(a)


# 4 - Utilizando fila ambas extremidades
deq = deque([20,40,60,80])
deq.appendleft(10)
print(deq)
deq.append(90)
deq.popleft()
deq.pop()
print(deq)

