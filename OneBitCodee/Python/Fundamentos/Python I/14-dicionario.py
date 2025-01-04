gameFifa = {
    "price": 90.55,
    "yearLaunch": 2022,
    "version": 2023,
    "classification": 8.5,
    "genre": ["esporte", "família"]
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

print(gameFifa["genre"])
print(gameFifa.get('classification'))

print(gameFifa.keys())
print(gameFifa.values())

print(gameFifa.items())

gameFifa["players"] = 2
print(gameFifa)

gameFifa.update({"players": 1})
print(gameFifa)

gameFifa.pop("players")