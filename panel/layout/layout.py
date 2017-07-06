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

    p.addSpdtSupercluster(1890, 100)
    p.addDpdtSupercluster(10900, 100, 4)
    p.addDpdtSupercluster(10900, 3520, 4)
    p.addMC(500, 3700)
    p.addSwitchSupercluster(2225, 3670)
    p.addLampSupercluster(6155, 5000)
    p.addDpdtSupercluster(9075, 100, 1)
    p.addVTiepointCluster(984, 3045)

    return p


##dwg = svgwrite.Drawing('test.svg', 
##        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
##        profile='full',
##        style=STYLE)

dwg = svgwrite.Drawing('panel-final.svg', 
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

dwg.save(pretty=True)

print p
