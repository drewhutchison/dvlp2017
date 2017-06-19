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
    p.addDpdtSupercluster(8300, 100, 2)
##    p.addInvertedDpdtSupercluster(15000, 3300, 22
    p.addDpdtSupercluster(12000, 100, 4)
    p.addDpdtSupercluster(12000, 3520, 4)
    p.addMC(1000, 3700)
    p.addSwitchSupercluster(3200, 3700)
    p.addHTiepointCluster(8300, 3500)
    p.addHTiepointCluster(8300, 4350)
    p.addLampSupercluster(7500, 5000)

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
p.drawMaskAreas(g)
##p.drawBoundboxes(g)

dwg.add(g)

dwg.save()
