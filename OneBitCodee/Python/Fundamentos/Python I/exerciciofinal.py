times = {
    
}


def AddTimes(times): 
    name = input("Qual vai ser o nome do time?")
    times[name] =[]

def RemoverTime(nome):
    name = input("Qual time você deseja remover?")
    for teams in times:
        if name == nome:
            del times[name]
    else:
        print("este time não existe")   


def listarTimes():
    for time in times:
        print(times)

        
                    