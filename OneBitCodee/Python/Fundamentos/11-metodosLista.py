gamesList = ["Fifa23", "Star Wars", "The Legend of Zelda", "Red Dead 2"]


print(len(gamesList))

print(gamesList.index("Fifa23"))

gamesList.append("God of War")
print(gamesList)

gamesList.sort()
print(gamesList)

gamesNew = gamesList.copy()
gamesNew.remove("Fifa23")
print(gamesNew)

gamesList.clear()
print(gamesList)