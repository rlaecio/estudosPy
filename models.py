# -*- coding: UTF-8 -*-
class Perfil(object):
    'classe padrão de perfis de usuarios comuns'
    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0


    def imprimir(self):
        print "Nome: %s, Telefone: %s, Empresa: %s" % (self.nome, self.telefone, self.empresa)


    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas

    def obter_creditos(self):
        if self.__tipo == 1:
            return self.__curtidas * 10.0

    @classmethod
    def gerar_perfis(classe, nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        perfis = []
        for linha in arquivo:
            valores = linha.split(',')
            if(len(valores) is not 3):
                raise ValueError('Uma linha no arquivo%s deve ter 3 valores' % nome_arquivo)
            perfis.append(classe(*valores))
        arquivo.close()
        return perfis




class Perfil_vip(Perfil):
    'Classe padrão para perfis de usuários vips'
    def __init__(self, nome, telefone, empresa, apelido=''):
        super(Perfil_vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

        
    def obter_creditos(self):
        return super(Perfil_vip, self).obter_curtidas() * 10.0



