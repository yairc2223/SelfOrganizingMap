import random
import numpy as np

class Matrix:

    def __init__(self, form):
        self.formation = form
        self.represent = None


    def set_marix(self, m):
        self.formation = m


    def set_representative(self, value):
        self.represent = value

    @staticmethod
    def get_random_matrix():
        grid = []
        for row in range(10):
            grid_rows = []
            for col in range(10):
                random_val = random.randint(0, 100) / 100
                grid_rows += [random_val]
            grid += [grid_rows]
        return Matrix(grid)

    @staticmethod
    def my_split(word):
        return [char for char in word]

    @staticmethod
    def parsematrices(filename, matrices_list):
        with open(filename, 'rb') as f:
            nx, ny = ...  # parse; advance file-pointer to data segment
            data = np.fromfile(f, dtype='>f8', count=nx * ny)
            array = np.reshape(data, [nx, ny], order='F')


    @staticmethod
    def parse_file_to_matrices_list(filename, matrices_list):
        f = open(filename, "r")
        buffer = []
        matrix = []

        for line in f:
            if len(line.strip()) == 0:
                buffer += [2]
            else:
                buffer += line.split()
        print(buffer)
        count = 0
        for row in buffer:
            if row == 2:
                matrices_list += [Matrix(matrix)]
                matrix = []
                count = 0
                continue
            row = Matrix.my_split(row)
            row = [int(i) for i in row]
            matrix += [row]
            count += 1
        f.close()
    @staticmethod
    def generate_neighbours_matrix():
        neighbours = [[0 for x in range(37)] for y in range(37)]
        # fill neighbours
        neighbours[0] = [3, 2, 1, 0, 2, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[1] = [2, 3, 2, 1, 1, 2, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[2] = [1, 2, 3, 2, 0, 1, 2, 2, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[3] = [0, 1, 2, 3, 0, 0, 1, 2, 2, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[4] = [2, 1, 0, 0, 3, 2, 1, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[5] = [2, 2, 1, 0, 2, 3, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[6] = [1, 2, 2, 1, 1, 2, 3, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[7] = [0, 1, 2, 2, 0, 1, 2, 3, 2, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[8] = [0, 0, 1, 2, 0, 0, 1, 2, 3, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[9] = [1, 0, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0,
                         0, 0, 0, 0, 0]
        neighbours[10] = [1, 1, 0, 0, 2, 2, 1, 0, 0, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0,
                          0,0, 0, 0, 0, 0]
        neighbours[11] = [1, 1, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0,
                          0,
                          0, 0, 0, 0, 0]
        neighbours[12] = [0, 1, 1, 1, 0, 1, 2, 2, 1, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0,
                          0,
                          0, 0, 0, 0, 0]
        neighbours[13] = [0, 0, 1, 1, 0, 0, 1, 2, 2, 0, 0, 1, 2, 3, 2, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0,
                          0,
                          0, 0, 0, 0, 0]
        neighbours[14] = [0, 0, 0, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 0, 1, 1, 0, 0, 0,
                          0,
                          0, 0, 0, 0, 0]
        neighbours[15] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 0, 1, 0, 0,
                          0,
                          0, 0, 0, 0, 0]
        neighbours[16] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 2, 2, 2, 0, 0, 0, 2, 3, 2, 1, 0, 0, 0, 2, 2, 1, 0, 0, 0, 1, 1, 0,
                          0,0, 0, 0, 0, 0]
        neighbours[17] = [0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 1, 1,
                          0,0, 0, 0, 0, 0]
        neighbours[18] = [0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 1,
                          1,0, 0, 0, 0, 0]
        neighbours[19] = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 0, 1, 2, 2, 1, 0, 0, 1,
                          1,1, 0, 0, 0, 0]
        neighbours[20] = [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 2, 3, 2, 0, 0, 0, 1, 2, 2, 0, 0, 0,
                          1,1, 0, 0, 0, 0]
        neighbours[21] = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 2, 0, 0, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1, 2, 0, 0, 0,
                          0,1, 0, 0, 0, 0]
        neighbours[22] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 0, 3, 2, 1, 0, 0, 0, 2, 1, 0,
                          0,0, 1, 0, 0, 0]
        neighbours[23] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 0, 0, 2, 3, 2, 1, 0, 0, 2, 2, 1,
                          0,0, 1, 1, 0, 0]
        neighbours[24] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2, 2,
                          1,0, 1, 1, 1, 0]
        neighbours[25] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 1, 0, 1, 2,
                          2,1, 0, 1, 1, 1]
        neighbours[26] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 0, 1, 2, 3, 2, 0, 0, 1,
                          2,2, 0, 0, 1, 1]
        neighbours[27] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 2, 2, 0, 0, 0, 1, 2, 3, 0, 0, 0,
                          1,2, 0, 0, 0, 1]
        neighbours[28] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 2, 2, 1, 0, 0, 0, 3, 2, 1,
                          0, 0, 2, 1, 0, 0]
        neighbours[29] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 0, 2, 3, 2,
                          1,0, 2, 2, 1, 0]
        neighbours[30] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 1, 0, 1, 2, 3,
                          2,1, 1, 2, 2, 1]
        neighbours[31] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1,0 , 0, 0, 1, 2, 2, 1, 0, 1, 2,
                          3,2, 0, 1, 2, 2]
        neighbours[32] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 2, 2, 0, 0, 1,
                          2,3, 0, 0, 1, 2]
        neighbours[33] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 2, 2, 1,
                          0,0, 3, 2, 1, 0]
        neighbours[34] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2, 2,
                          1,0, 2, 3, 2, 1]
        neighbours[35] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 2,
                          2,1, 1, 2, 3, 2]
        neighbours[36] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1,
                          2,2, 0, 1, 2, 3]
        return neighbours

    @staticmethod
    def neighbours_test(neighbours):
        for index, l in enumerate(neighbours):
            print("neighbours of  {0} are: ".format(index + 1))
            for index2, i in enumerate(l):
                if i == 1:
                    print(index2 + 1)

