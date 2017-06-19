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

class Lamp(Component):
    r_exclude = 960/2
    r_mask = 814/2

class Switch(Component):
    '''NKK M2015SS1W01, Jameco part no 2258777'''

    r_mask = 315/2
    height = 512
    width = 311

    @property
    def excludedElement(self):
        return shapes.Rect((self.x - self.width/2, self.y - self.height/2),
                (self.width, self.height))

    @property
    def maskedElement(self):
        return shapes.Circle((self.x, self.y), self.r_mask)
