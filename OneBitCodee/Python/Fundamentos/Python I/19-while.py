gameName = input("Digite o nome do jogo\\n")
qtdRating = 0
totalRating = 0
rating = 0
average = 0
while(rating != -1):
    rating = float(input("Informe a nota: "))
    if(rating!= -1):
        totalRating += rating
        qtdRating += 1
        average = totalRating / qtdRating
print(f"media das avaliações do jogo {gameName} é {average: .2f}")        