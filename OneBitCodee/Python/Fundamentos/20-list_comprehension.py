listNumbers = [i for i in range(10) if i< 4]
print(listNumbers)

doubled = [i * 2 for i in range(5)]
# Resultado: [0, 2, 4, 6, 8]


squares = [i ** 2 for i in range(10) if i % 2 != 0]
# Resultado: [1, 9, 25, 49, 81] (quadrados dos números ímpares)


evens = [i for i in range(10) if i % 2 == 0]
# Resultado: [0, 2, 4, 6, 8]

gamesList = ["Mario Odyssey", "Donkey Kong Country", "Luigi's mansion", "Kirby"]

newList = [x for x in gamesList if "a" in x]
print(newList)
