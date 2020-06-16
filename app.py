# -*- coding: UTF-8 -*-


def listar(nomes):
    print 'Listando nomes:'
    for nome in nomes:
        print nome
        
        
def cadastrar(nomes):
    print 'Digite: o nome:'
    nome = raw_input()
    nomes.append(nome)

def remover(nomes):
    print 'Digite o nome a remover:'
    nome = raw_input()
    nomes.remove(nome)

def alterar(nomes):
    print 'Informe o nome que deseja alterar:'
    nome = raw_input()
    if(nome in nomes):
        print 'Informe o novo nome:'
        indice = nomes.index(nome)
        nome = raw_input()
        nomes[indice] = nome
        
def procurar(nomes):
    print 'Digite o nome a procurar'
    nome = raw_input()
    if(nome in nomes):
        indice = nomes.index(nome)
        print "O nome %s foi localizado no indice " %(nome) + str(indice)
    else:
        print "O nome %s não foi localizado na lista!" % (nome)


        
def menu():
    nomes = []
    escolha = ''
    while(escolha != '0'):
        print 'Digite: 1->cadastrar, 2->listar, 3->remover, 4->alterar, 5->pesquisar, 0->terminar'
        escolha = raw_input()

        if(escolha == '1'):
            cadastrar(nomes)

        if(escolha == '2'):
            listar(nomes)

        if(escolha == '3'):
            remover(nomes)

        if(escolha == '4'):
            alterar(nomes)

        if(escolha == '5'):
            procurar(nomes)
            


menu()
