idade = int(input('Digite sua idade: '))

if (idade > 18 ):
    print('Você é maior de idade!')
else:
    if(idade < 12):
        print('Você é uma criança, só tem {} anos!' .format(idade))
    elif(idade > 12):
        print('Você é um adolescente!')
12