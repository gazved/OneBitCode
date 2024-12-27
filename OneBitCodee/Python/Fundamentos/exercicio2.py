#principal = input("Digite a sua string: ")
#letra1 = principal[:1]
#secundaria = principal[1:]
#main = letra1 + secundaria.replace(letra1, "#")
#print(main)


str1 = input("primeira string: ")
str2 = input("segunda string: ")
comeco1 = str1[:2]
comeco2 = str2[:2]
main = str1.replace(comeco1, comeco2)+" "+ str2.replace(comeco2, comeco1)
print(main)
