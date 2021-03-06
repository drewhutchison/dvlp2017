from svgwrite import shapes, text

NaN = float('NaN')

class Component(object):
    r_exclude = None
    r_mask = None
    panel_offset_x = NaN
    panel_offset_y = NaN

    def __init__(self, x, y, name='unnamed'):
        self.x = x
        self.y = y
        self.name = name

    def __str__(self):
        return '{} instance "{}" at ({},{}) [drawing], ({}, {}) [panel]'.format(
            self.__class__.__name__,
            self.name,
            self.x,
            self.y,
            self.x - self.panel_offset_x,
            self.panel_offset_y - self.y
        )

    @property
    def excludedElement(self):
        return shapes.Circle((self.x, self.y),
                self.r_exclude, 
                class_='exclusion {}'.format(self.__class__.__name__)
                )

    @property
    def maskedElement(self):
        return shapes.Circle((self.x, self.y),
                self.r_mask,
                class_='mask {}'.format(self.__class__.__name__),
                id=self.name
                )

    @property
    def textElement(self):
        return text.Text(self.name,
                (self.x, self.y),
                font_size=150,
                font_family='monospace')

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
                (self.width, self.height),
                class_='exclusion {}'.format(self.__class__.__name__)
                )

    @property
    def maskedElement(self):
        return shapes.Circle((self.x, self.y), 
                self.r_mask,
                class_='mask {}'.format(self.__class__.__name__)
                )

class Keyswitch(Component):
    r_exclude = 1081/2
    r_mask = 868/2

class Fuse(Component):
    r_exclude = 760/2
    r_mask = 760/2

class Standoff(Component):
    '''
    #8 flathead countersunk screw protruding from front-side.
    Exclusion area is knockout, mask area is edge of countersink.
    Measurements are from https://www.guden.com/StaticHtml/Countersink/
    '''
    r_exclude = 187/2
    r_mask = 320/2
