import numpy as np
from colors import bcolors
from matrix_utility import print_matrix
from inverse_matrix import get_elemetarys


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    return norm_A


if __name__ == '__main__':
    A = np.array([[1, 1/2, 1/3],
                  [1/2, 1/3 , 1/4],
                  [1/3, 1/4, 1.5]])
    B=[]
    B= get_elemetarys(A)

    print("The max norm of A is: ", condition_number(A))
    print("-----------------------------")
    print("The last 3 elementary matrices are: ")
    for mat in B[-3:]:
        print(mat)
        print("-----------------------------")

    print("Date: 19/02/24")
    print(
        "Group: Haim Armias - 315569061, Yehuda Baza - 208029819, Rahamim Tadela - 208189621, Orel Achrak - 318554532")
    print("Git: https://github.com/OrelAchrak/Analiza/tree/master")
    print("Name: Rahamim Tadela - 208189621")





