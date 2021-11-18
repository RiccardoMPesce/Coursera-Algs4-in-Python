from week1.WeightedQuickUnionUF import WeightedQuickUnionUF

class Percolation:
    def __init__(self, n):
        self.n = n
        self.grid = WeightedQuickUnionUF(n * n)

    def open(self, row, col):
        pass
    
    def is_open(self, row, col):
        return self.grid[row - 1][col - 1] == 0

    def is_full(self, row, col):
        return self.grid[row - 1][col - 1] == 1

    def number_of_open_sites(self):
        return sum([sum([int(cell == 0) for cell in r]) for r in self.grid])

    def percolates(self):
        pass 

