from SOAPpy import *

cont = 0

class Sala(object):
	"""docstring for Sala"""
	def __init__(self,num):
		super(Sala, self).__init__()
		self.num = num
	
	def iniciaHorario(self):
		self.horarios = [i for i in range(8,23)]

	def reserva(self,horario):
		self.horarios.remove(horario) 

	def libera(self,horario):
		self.horarios.append(horario)
		self.horarios.sort()

	def consulta(self):
		return self.horarios

	def getNum(self):
		return self.num

class Salas(object):
	"""docstring for Salas"""
	def __init__(self):
		super(Salas, self).__init__()
		self.salas = []

	def adicionaSala(self,sala):
		self.salas.append(sala)

	def status(self):

		status =  '\n--------------------------------------------------------------------'
		status += '\nStatus:\n'

		for sala in self.salas:
			status += '\n\nNumero: ' + str(sala.getNum()) + '\n'
			status += '\nHorarios Disponiveis: \n'

			status += '[' + ", ".join(map(str,sala.consulta())) + ']'
			
		return status
		

	def reservaSala(self,numSala, horario):

		for sala in self.salas:

			if sala.getNum() == numSala:
				sala.reserva(horario)

	def liberaSala(self, numSala, horario):

		for sala in self.salas:

			if sala.getNum() == numSala:
				sala.libera(horario)

def reservaSala(numSala, horario):
	global salas
	salas.reservaSala(numSala, horario)

def liberaSala(numSala, horario):
	global salas
	salas.liberaSala(numSala, horario)

def criaSala():
	
	global cont
	global salas

	sala = Sala(cont)

	sala.iniciaHorario()

	salas.adicionaSala(sala)

	cont += 1

def iniciaSalas():

	global cont
	global salas

	for i in range(3):

		criaSala()

def menu():

	menu = "--------------------------------------------------------------------\n"
	menu += "Menu\n"
	menu += "Digite o codigo da opcao desejada: \n\n"
	menu += "1 - Ver status da sala\n"
	menu += "2 - Reservar uma sala\n"
	menu += "3 - Liberar uma sala\n"
	menu += "0 - Sair\n"

	return menu

def status():

	global salas

	return salas.status()

def consulta(nSala):

	global salas

	return salas.salas[nSala].consulta()

salas = Salas()

iniciaSalas()

server = SOAPServer(('localhost', 1111))
server.registerFunction(status)
server.registerFunction(menu)
server.registerFunction(consulta)
server.registerFunction(liberaSala)
server.registerFunction(reservaSala)
server.serve_forever()