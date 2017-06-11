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

# Default style
STYLE = '''
    stroke: black;
    stroke-width: 10;
    fill-opacity: 0;
'''

def get_panel():

    p = Panel()

    p.addSpdtSupercluster(1000, 100)
    p.addDpdtSupercluster(9000, 100, 6)
    p.addInvertedDpdtSupercluster(15000, 3300, 2)
    p.addMC(1000, 3700)
    p.addSwitchSupercluster(3500, 3700)
    p.addHTiepointCluster(7000, 3700)

    return p


##dwg = svgwrite.Drawing('test.svg', 
##        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
##        profile='full',
##        style=STYLE)

dwg = svgwrite.Drawing('test.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full')

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))

dwg.add_stylesheet('default.css', 'default')

g = svgwrite.container.Group()

p = get_panel()

p.drawFrame(g)
p.drawExclusionAreas(g)
p.drawBoundboxes(g)

dwg.add(g)

dwg.save()
