#Write a library that contains a class that can represent any 2x2 real matrice. 
#Include two functions to calculate the sum and product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
#Examples:
#
# matrix_1 = Matrix(4,5,6,7)
# matrix_2 = Matrix(2,2,2,1)
#
# matrix_3 = matrix_2.add(matrix_1)
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#(If you want you can expand implementation to NxN matrix.)
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be named "kol_gr2"! 
#
#Delete these comments before commit!
#Good luck.

#!/usr/bin/python


from matrix import Matrix


def main():

	print "matrices"

	mat_1, mat_2 = [], []
		
	for i in range(0, 3): # wiersze
		mat_1.append([])
		mat_2.append([])
		for j in range(0, 3): # kolumny
			mat_1[i].append(2)
			mat_2[i].append(3)

	matrix_1 = Matrix(3, mat_1)
	matrix_2 = Matrix(3, mat_2)

	matrix_1.print_out()


if __name__ == "__main__":
	main()


