class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        self._size = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
