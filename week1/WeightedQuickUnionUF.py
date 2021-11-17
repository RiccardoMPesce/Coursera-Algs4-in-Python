class WeightedQuickUnionUF:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]
        self._size = [1] * n

    @property
    def count(self):
        return self._count