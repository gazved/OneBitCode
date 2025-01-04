gamesSet = {"Fifa23", "Red Dead 2", "Star Wars", "The Legend of Zelda", "Red Dead 2"}

grupo1 = {1, 2, 3, 4}
grupo2 = {4, 5, 6}
print(grupo1 & grupo2)#elementos em comumn
print(grupo1 | grupo2)#junta tudo, uniao
#ignora elementos repetidos
print(grupo1 ^ grupo2)#mostra todos elementos, menos os repetidos

#true e 1 sao considerados o mesmo valor, alem de -1 e false

exampleSet = {"Fifa23", True, 1, 90.50} 
print(exampleSet)

# 2 - Adicionando item no set
gamesSet.add("Resident Evil 4")
print(gamesSet)

# 3 - Adicionando item de outro set
gamesSet.update(exampleSet)
print(gamesSet)