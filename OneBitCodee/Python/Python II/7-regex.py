import re


#Índice final e inicial de uma palavra
#O r significa que estamos trabalhando com uma string bruta (raw string)

text = 'OneBitCode: Transformamos pessoas em programadores sem limites'
match = re.search(r'pessoas', text)

print("indice inicial: ", match.start())


#buscar onde fica o ponto

site = "www.pucminas.com"
match = re.search(r'\.', site)

print(match)

#buscando uma lista de caracteres em uma frase

padrao = "[a-m]"

result = re.findall(padrao, text)
print(result)

#verificando o inicio de uma string

rule = r'^A'
phrases = ['A casa está suja', 'O dia está lindo', 'Vamos passear']

for f in phrases:
    if re.match(rule, f):
        print(f"corresponde: {f}")
    else:
        print(f"não corresponde: {f}")    

