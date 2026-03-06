#classeś with super
class Object:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

class Circle(Object):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius

kreis = Circle(color="red",filled=True,radius=10)
print(kreis.color)