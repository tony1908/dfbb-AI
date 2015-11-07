from puzzle import *
from nodes import *

stack = []
mymatrix=[[5,1,3,4],[0,2,6,8],[9,10,7,12],[13,14,11,15]]
stack2 = [mymatrix]
lista = []
final = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
limit = 17
resul = ''
encontrado = False
node = Nodo(mymatrix)
stack.append(node)
while (encontrado != True) and (len(stack) > 0) :
	temp = stack.pop()
	nivel = temp.nivel
	pad = temp.padre
	i,j = posicion(temp.valor)
	print temp.valor[:]
	iz = moverIzquierda(temp.valor[:],i,j)
	de = moverDerecha(temp.valor[:],i,j)
	ar = moverArriba(temp.valor[:],i,j)
	ab = moverAbajo(temp.valor[:],i,j)
	izq = Nodo(iz,temp,nivel+1)
	der = Nodo(de,temp,nivel+1)
	arr = Nodo(ar,temp,nivel+1)
	aba = Nodo(ab,temp,nivel+1)
	if temp.valor[:] == final:
		print "Respuesta encontrada"
		resul = temp
		# print temp.padre.valor
		encontrado = True
		print resul.nivel
	elif temp.nivel+1 <= limit:
		if izq.valor != None and stack2.count(izq.valor) == 0:
			stack.append(izq)
			stack2.append(izq.valor)
		if der.valor != None and stack2.count(der.valor) == 0:
			stack.append(der)
			stack2.append(der.valor)
		if arr.valor != None and stack2.count(arr.valor) == 0:
			stack.append(arr)
			stack2.append(arr.valor)
		if aba.valor != None and stack2.count(aba.valor) == 0:
			stack.append(aba)
			stack2.append(aba.valor)

if encontrado == True:
	print "Camino:"
	print resul.valor
	while(resul.padre != None):
		print resul.padre.valor
		resul = resul.padre
		pass
