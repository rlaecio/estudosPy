idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12

print('{}, {}, {}' .format(maior_idade, crianca, adolescente))
