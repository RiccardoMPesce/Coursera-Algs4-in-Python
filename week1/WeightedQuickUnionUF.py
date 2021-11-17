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

    def connected(self, p, q):
        self.find(p) == self.find(q)

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        if root_p == root_q:
            return 

        if self._size[root_p] < self._size[root_q]:
            self._parent[root_p] = root_q
            self._size[root_q] += self._size[root_p]
        else:
            self._parent[root_q] = root_p
            self._size[root_p] += self._size[root_q]

        self._count -= 1

def main():
    pass 

if __name__ == "__main__":
    main()