class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() + other.get_area()
        elif isinstance(other, Square):
            return self.get_area() + other.get_area()
        else:
            raise TypeError("Unsupported operand for +")

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        if isinstance(other, Rectangle):
            return self.get_area() + other.get_area()
        elif isinstance(other, Square):
            return self.get_area() + other.get_area()
        else:
            raise TypeError("Unsupported operand for +")


def main():
    s = Square(5)
    r = Rectangle(8, 2)

    print(f"square area = {s.get_area()}")
    print(f"rectangle area = {r.get_area()}")

    print(f"aggregated area is: {s + r}")
if __name__ == "__main__":
    main()
