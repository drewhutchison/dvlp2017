from svgwrite import shapes

class Component(object):
    r_exclude = None
    r_mask = None

    def __init__(self, x, y, name='unnamed'):
        self.x = x
        self.y = y
        self.name = name

    @property
    def excludedElement(self):
        return shapes.Circle((self.x, self.y), self.r_exclude)

    @property
    def maskedElement(self):
        return shapes.Circle((self.x, self.y), self.r_mask)

class Jack(Component):
    r_exclude = 770/2
    r_mask = 591/2

