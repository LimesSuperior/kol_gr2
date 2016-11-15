#!/usr/bin/python


class MatrixError(Exception):
	pass

class Matrix(object):

	def __init__(self, n, fill=False, fill_value=0):

		if type(fill) is not bool:
			raise TypeError('Matrix __init__: fill parameter must be bool type')

		if type(fill_value) is not float and type(fill_value) is not int:
			raise TypeError('Matrix __init__: fill_value parameter must be float or int type')

		if fill:
			self.rows = [[fill_value]*n for x in range(n)]
		else:
			self.rows = []
		self.n = n

	def __getitem__(self, index):

		return self.rows[index]

	def __setitem__(self, index, value):

		self.rows[index] = value

	def __add__(self, matrix):
		
		if self.n != matrix.n:
			raise MatrixError, "Matrix __add__: Size must match"

		result = Matrix(self.n, fill=True, fill_value=0)

		for x in range(self.n):
			row = [sum(value) for value in zip(self.rows[x], matrix[x])]
			result[x] = row

		return result

	def __mul__(self, matrix):

		if self.n != matrix.n:
			raise MatrixError, "Matrix __add__: Size must match"
        
		transposed = matrix.transposed()
		result = Matrix(self.n, fill=True)
        
		for x in range(self.n):
			for y in range(transposed.n):
				result[x][y] = sum([item[0]*item[1] for item in zip(self.rows[x], transposed[y])])

		return result

	def transposed(self):

		matrix = Matrix(self.n, fill=True)
		matrix.rows = [list(item) for item in zip(*self.rows)]

		return matrix

	def __str__(self):
		s='\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
		return s + '\n'
			

		 
