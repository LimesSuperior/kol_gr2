#!/usr/bin/python


class Matrix(object):
# macierz kwadratwa NxN

	_matrix = [] # macierz w postaci listy N list o rozmiarze N kazda

	# N - wymiar macierzy
	# matrix - macierz w postaci listy N list o rozmiarze N kazda
	def __init__(self, N, matrix):

		self.N = N

		# kopiowanie
		for i in range(0, N): # wiersze
			self._matrix.append([])
			for j in range(0, N): # kolumny
				self._matrix[i].append(matrix[i][j])

	# mnozenie dwoch macierzy NxN
	def multiply(self, second_matrix):

		if self.N != second_matrix.N:
			return
			
		product_matrix = Matrix(self.N, tmp)

		for i in range(0, N):
			for j in range(0, N):
				current_sum = 0
				for k in range (0, N):
					current_sum += self._matrix[i][k]  * second_matrix._matrix[k][j]

		return product_matrix

	def print_out(self):
		for i in range(0, self.N): # wiersze
			for j in range(0, self.N): # kolumny
				print self._matrix[i]



