class Block:

    def __init__(self, width: int, length: int, height: int):
        self.width = width
        self.length = length
        self.height = height

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_height(self):
        return self.height

    def get_volume(self):
        return self.height * self.width * self.length

    def get_surface_area(self):
        return ((self.height * self.length) + (self.height * self.width) + (self.length * self.width)) * 2

block1 = Block(2, 2, 2)