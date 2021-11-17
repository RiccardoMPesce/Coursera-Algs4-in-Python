class WeightedQuickUnionUF:
    def __init__(self, n):
        self._count = n
        self._parent = [i for i in range(n)]
        self._size = [1] * n

    def count(self):
        return self._count

    def validate(self, p):
        n = len(self._parent)
        if p < 0 or p > n - 1:
            raise IndexError(f"index is not between {0} and {n - 1}")

    def find(self, p):
        self.validate(p)
        while (p != self._parent[p]):
            p = self._parent[p]
        return p