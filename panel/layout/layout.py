'''
layout.py

lays out panel artwork

Dimensions in thousandths of an inch except where noted.
'''

import svgwrite

# Drawing size
# These in inches
WIDTH = 21
HEIGHT = 14

# Default style, will be moved
STYLE = '''
    stroke: black;
    stroke-width: 10;
    fill-opacity: 0;
'''

class Panel(object):

    # hardcoded lower-left-hand-corner origin in user coords
    X = 1000
    Y = 9000
    
    # hardcoded width figures
    fullwidth = 19000
    inclusionwidth = 17500

    # nominal height in rack units
    nU = 5

    # allow 1/32in slop
    height = 1750 * nU - 31

    def __init__(self):
        self.clusters = []

    def drawFrame(self, addable):
        addable.add(svgwrite.shapes.Rect(
            (self.X, self.Y-self.height), 
            (self.X + self.fullwidth, self.height)))
        addable.add(svgwrite.shapes.Rect(
            (self.X + (self.fullwidth-self.inclusionwidth)/2, self.Y-self.height), 
            (self.X + self.inclusionwidth, self.height)))

    def addSpdtSuperCluster(self, x, y):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(SpdtSuperCluster(self.X + x, self.Y - y))

    def drawExclusionAreas(self, addable):
        for cluster in self.clusters:
            cluster.addExclusions(addable)
    
class Component(object):
    r_exclude = None
    r_mask = None

    def __init__(self, x, y, name='unnamed'):
        self.x = x
        self.y = y
        self.name = name

    @property
    def excludedElement(self):
        print self.x, self.y, self.name
        return svgwrite.shapes.Circle((self.x, self.y), self.r_exclude)

    @property
    def maskedElement(self):
        return svgwrite.shapes.Circle((self.x, self.y), self.r_mask)

class Jack(Component):
    r_exclude = 770/2
    r_mask = 591/2

class SpdtCluster(object):
    '''this should originate from the bottom left-hand corner of the 
    bottommost jack's padded area'''

    hpad = 50
    vpad = 100

    def __init__(self, x, y, name='unnamed'):

        v_centerline = x + Jack.r_exclude
        h_baseline = y

        self.components = [
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude,
                name+'.NC'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NO'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.COM'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 7 - self.vpad * 3,
                name+'.COIL')
        ]

    def addExclusions(self, addable):
        for c in self.components:
            addable.add(c.excludedElement)

    def addBoundBox(self, addable):
        addable.add(self.bbox)

class SpdtSuperCluster(object):

    def __init__(self, x, y):
        self.clusters = [
                SpdtCluster(x + (i*1000), y)
                for i in range (8)
                ]

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

dwg = svgwrite.Drawing('test.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full',
        style=STYLE)

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))

g = svgwrite.container.Group()

p = Panel()

p.drawFrame(g)

p.addSpdtSuperCluster(1000, 100)
p.drawExclusionAreas(g)

dwg.add(g)

dwg.save()
