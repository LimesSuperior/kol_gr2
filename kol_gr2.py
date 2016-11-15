#!/usr/bin/python


from matrix import Matrix


def main():

	my_matrix1 = Matrix(n=3, fill=True, fill_value=8.8)
	my_matrix2 = Matrix(n=3, fill=True, fill_value=10)
	my_matrix3 = my_matrix1 + my_matrix2
	print my_matrix1, my_matrix2, my_matrix3

	my_matrix4 = Matrix(n=4, fill=True, fill_value=1)
	my_matrix5 = Matrix(n=4, fill=True, fill_value=1)
	my_matrix6 = my_matrix4 * my_matrix5
	print my_matrix6


if __name__ == "__main__":
	main()


