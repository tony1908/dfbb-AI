def posicion(matrix):#funcion para obtener la posicion
	pos1 = 0
	pos2 = 0
	for mat in matrix:
	    for x in mat:
	        if x == 0:
	        	pos1 = matrix.index(mat)
	        	pos2 = mat.index(x)
	return pos1,pos2

def moverIzquierda(matrix,x,y):#x = i, y =j
	if (y - 1) >= 0:
		matrix_temp = matrix[x][:]
		matrix_temp[y-1], matrix_temp[y] = 0, matrix_temp[y-1]
		matrix[x] = matrix_temp
		return matrix
	else:
		return None

def moverDerecha(matrix, x, y):
    size = len(matrix) - 1
    if (y + 1) <= size:
        matrix_temp = matrix[x][:]
        matrix_temp[y+1], matrix_temp[y] = 0, matrix_temp[y+1]
        matrix[x] = matrix_temp
        return matrix
    else:
        return None

def moverArriba(matrix, x, y):
	if (x - 1)>=0:
		matrix_temp = matrix[x-1][:]
		matrix_temp1 = matrix[x][:]
		matrix_temp[y], matrix_temp1[y] = 0, matrix_temp[y]
		matrix[x-1] = matrix_temp
		matrix[x] = matrix_temp1
		return matrix
	else:
		return None

def moverAbajo(matrix,x,y):
	size = len(matrix) - 1
	if (x + 1) <= size:
		matrix_temp = matrix[x+1][:]
		matrix_temp1 = matrix[x][:]
		matrix_temp[y], matrix_temp1[y] = 0, matrix_temp[y]
		matrix[x+1] = matrix_temp
		matrix[x] = matrix_temp1
		return matrix
	else:
		return None


