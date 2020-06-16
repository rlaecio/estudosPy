# -*- coding: UTF-8 -*-
class Perfil(object):
    def __init__(self, nome, telefone, empresa): 
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)


class Data(object):
   def __init__(self, dia, mes, ano):
      self.dia = dia
      self.mes = mes
      self.ano = ano

   def imprime(self):
      print '%s/%s/%s' % (self.dia, self.mes, self.ano)


class Pessoa(object):
    def __init__(self, nome, peso, altura):
        self.nome = nome
		self.peso = peso
		self.altura = altura

    def calcula(self):
		quadrado = self.altura * self.altura
		resultado = self.peso / quadrado
		print 'O IMC do %s é %s' % (self.nome, resultado)