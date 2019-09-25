import math


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        result = self.height * self.width
        print(f'{result:.2f}')

    def diagonal(self):
        result = math.sqrt(self.height ** 2 + self.width ** 2)
        print(f'{result:.2f}')


def main():
    rectangle1 = Rectangle(height=5, width=6)
    rectangle1.area()
    rectangle1.diagonal()


if __name__ == "__main__":
    main()
