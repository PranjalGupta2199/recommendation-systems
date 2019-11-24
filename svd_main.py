import numpy
import pickle
import svd

if __name__ == "__main__":
    input_matrix = numpy.array([
        [1, 1, 1, 0, 0],
        [3, 3, 3, 0, 0],
        [4, 4, 4, 0, 0],
        [5, 5, 5, 0, 0],
        [0, 2, 0, 4, 4],
        [0, 0, 0, 5, 5],
        [0, 1, 0, 2, 2]])
    a = svd.model.SVD(input_matrix)
    a.decompose()
    a.reconstruct()
    print(a.get_rms_error())
