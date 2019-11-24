import svd
import pickle
import cur
import numpy as np
import math
import time

def loadFile(filename):
    '''
    Loads file saved after running preprocess.py.
    return: opened file object
    '''
    file = open(filename, 'rb')
    filename = pickle.load(file)
    return filename


def calculate_rmse(matrix_1, matrix_2):
    """
    Calculate rmse between matrix 1 and 2
    """
    error = 0
    for i in range(matrix_1.shape[0]):
        for j in range(matrix_1.shape[1]):
            error = error + ((matrix_1[i][j] - matrix_2[i][j])*(matrix_1[i][j] - matrix_2[i][j]))

    return error / ((matrix_1.shape[0] * matrix_1.shape[1]))


def calculate_mae(matrix_1, matrix_2):
    """
    Calculate mae between matrix 1 and 2
    """
    error = 0
    for i in range(matrix_2.shape[0]):
        for j in range(matrix_2.shape[1]):
            error = error + (abs(matrix_1[i][j] - matrix_2[i][j]))

    return error / ((matrix_1.shape[0] * matrix_1.shape[1]))


if (__name__ == "__main__"):
    a = time.time()
    utility_matrix = loadFile("utility")
    
    # CUR Decomposition
    rmse = 0
    mae = 0
    for i in range(10, 11):
        C, U, R = cur.calculate_cur(utility_matrix, i)
        result = np.matmul(C, np.matmul(U, R))
        print(result.shape[0], result.shape[1])
        print(utility_matrix.shape[0], utility_matrix.shape[1])
        print(result)

        for i in range(len(result)):
            for j in range(len(result[0])):
                if result[i][j] > 5:
                    result[i][j] = 0
                elif result[i][j] < 0:
                    if ((abs(result[i][j]) > 0) and (abs(result[i][j]) < 5)):
                        result[i][j] = abs(result[i][j])
                    else:
                        result[i][j] = 0 

        error_rmse = calculate_rmse(utility_matrix, result)
        error_mae = calculate_mae(utility_matrix, result)
        rmse = rmse + math.sqrt(error_rmse)
        mae = mae + error_mae        

    b = time.time()
    print(rmse)
    print(mae)
    print(b - a)