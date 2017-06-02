'''
layout.py

lays out panel artwork

Dimensions in thousandths of an inch except where noted.
'''

import svgwrite

from assets import Panel

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

def get_panel():

    p = Panel()

    p.addSpdtSupercluster(1000, 100)
    p.addDpdtSupercluster(9000, 100)
    p.addDpdtSupercluster(9000, 3500)
    p.addMC(1000, 3500)

    return p


dwg = svgwrite.Drawing('test.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full',
        style=STYLE)

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))

g = svgwrite.container.Group()

p = get_panel()

p.drawFrame(g)
p.drawExclusionAreas(g)
p.drawBoundboxes(g)

dwg.add(g)

dwg.save()
