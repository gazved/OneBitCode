import re
main = input('Digite a frase desejada:\n')
rule1 = '[a-z]'
rule2 = '[A-Z]'
rule3 = '[1-9]'

match = re.search(main, rule1)

def check(string):
    rule = re.compile
    


def check_character(string):
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return not bool(string)

print(check_character("ABCDEFabcdef123450")) 
print(check_character("*&%@#!}{"))






email = "usuario@exemplo.com"
padrao_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
if re.match(padrao_email, email):
    print("E-mail válido!")
else:
    print("E-mail inválido!")
    
    
    
padrao = re.compile(r"\d+")
texto1 = "123 abcd"
texto2 = "456 efgh"
print(padrao.findall(texto1))  # Saída: ['123']
print(padrao.findall(texto2))  # Saída: ['456']



texto = "Os números são 10, 20 e 30."
numeros = re.findall(r"\d+", texto)
print(numeros)  # Saída: ['10', '20', '30']


import re
texto = "Meu número é 123-456-7890"
padrao = r"\d{3}-\d{3}-\d{4}"  # Padrão para número no formato XXX-XXX-XXXX
resultado = re.search(padrao, texto)
if resultado:
    print("Número encontrado:", resultado.group())
    



