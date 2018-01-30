from SOAPpy import *

loop = True

server = SOAPProxy('http://localhost:1111/')

while loop:

	print server.menu()

	request = input()

	if str(request) == '1':

		print str(server.status())

	elif str(request) == '2':

		print "Qual sala deseja reservar?"
		nSala = int(input())
		
		print	("\nHorario Disponiveis:\n" +
					 "[" + ", ".join(map(str, server.consulta(nSala)))+ "]" +'\n\n' + 
					 "Informe o horario da sala que deseja reservar:")

		horario = int(input())
		
		server.reservaSala(nSala, horario)

	elif str(request) == '3':

		print("Qual sala deseja liberar?")
		nSala = int(input())
		
		print("Horario da sala a liberar: ")
		horario = int(input())

		server.liberaSala(nSala, horario)

	elif str(request) == '0':

		loop = False

		print("Saindo!")