class Rectangle:

    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}


# Testing
rect = Rectangle(20, 7)

for item in rect:
    print(item)