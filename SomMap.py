from Cell import *
from MyMatrix import *


class SomMap:

    def __init__(self, form):
        self.formation = form

    @staticmethod
    def initialize_som_map():
        cells_list = []
        for i in range(1, 38):
            new_cell = Cell(i, Matrix.get_random_matrix(), 0)
            cells_list += [new_cell]
        return SomMap(cells_list)

    def getCellMatrixbyIndex(self,indeex):
        for i in self.formation:
            d=1
