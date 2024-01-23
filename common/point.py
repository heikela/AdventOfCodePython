class Point2D():
    """An immutable 2D point class"""

    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return f"Point2D({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def orthogonal_neighbours(self):
        """Returns the 4 orthogonal neighbours of this point"""
        yield self + Point2D.up
        yield self + Point2D.left
        yield self + Point2D.right
        yield self + Point2D.down

    def neighbours(self):
        """Returns the 8 neighbours of this point"""
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                yield self + Point2D(dx, dy)


Point2D.left = Point2D(-1, 0)
Point2D.right = Point2D(1, 0)
Point2D.up = Point2D(0, -1)
Point2D.down = Point2D(0, 1)
