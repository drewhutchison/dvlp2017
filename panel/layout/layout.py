'''
layout.py

lays out panel artwork

Dimensions in thousandths of an inch except where noted.
'''

import svgwrite

from superclusters import *

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
    nU = 4

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

    def addSpdtSupercluster(self, x, y):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(SpdtSupercluster(self.X + x, self.Y - y))

    def addDpdtSupercluster(self, x, y):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(DpdtSupercluster(self.X + x, self.Y - y))

    def drawExclusionAreas(self, addable):
        for cluster in self.clusters:
            cluster.addExclusions(addable)
    
dwg = svgwrite.Drawing('test.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full',
        style=STYLE)

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))

g = svgwrite.container.Group()

p = Panel()

p.drawFrame(g)

p.addSpdtSupercluster(1000, 100)
p.addDpdtSupercluster(9000, 100)
p.addDpdtSupercluster(9000, 3500)
p.drawExclusionAreas(g)

dwg.add(g)

dwg.save()
