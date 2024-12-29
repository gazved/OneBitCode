import pprint
gamesDict = {
  "fifa 23" : {
    "yearLaunch" : 2022,
    "classification" : 8.5,
    "genre": ["esporte", "família"]
  },
  "mario odyssey" : {
    "yearLaunch" : 2017,
    "classification" : 10.0,
    "genre": ["aventura", "3d"]
  },
  "donkey kong country" : {
    "yearLaunch" : 1996,
    "classification" : 9.5,
    "genre": ["aventura", "plataforma"]
  }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

gamesDict["donkey kong country"]["Players"] = 2
print(gamesDict["donkey kong country"])


del gamesDict["fifa 23"]