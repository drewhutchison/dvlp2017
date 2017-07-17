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

STYLE = '''
    fill: blue;
    stroke: none;
'''

def get_panel():

    p = Panel()

    p.addSpdtSupercluster(1890, 100)
    p.addDpdtSupercluster(10900, 100, 4, start=13)
    p.addDpdtSupercluster(10900, 3520, 4, start=9)
    p.addMC(500, 3700)
    p.addSwitchSupercluster(2225, 3670)
    p.addLampSupercluster(6155, 5000)
    p.addDpdtSupercluster(9075, 100, 1, start=1, label='TR')
    p.addVTiepointCluster(984, 2175)
    p.addStandoffs(2995, [1250, 9250, 17750])

    return p


## composite drawing. all layers, viewable in browser w/ external css

dwg = svgwrite.Drawing('panel-final-composite.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full')

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))
dwg.add_stylesheet('default.css', 'default')

g = svgwrite.container.Group()

p = get_panel()

p.drawFrame(g)
p.drawExclusionAreas(g)
p.drawMaskAreas(g)
p.drawLabels(g)

dwg.add(g)

dwg.save(pretty=True)

print p

## drawing for illustrator, just frame and mask areas with document-specified
## fill


dwg = svgwrite.Drawing('panel-final-masks.svg', 
        size=(WIDTH*svgwrite.inch, HEIGHT*svgwrite.inch),
        profile='full',
        style=STYLE)

dwg.viewbox(width=int(WIDTH*1000), height=int(HEIGHT*1000))

g = svgwrite.container.Group()

p = get_panel()

p.drawFrame(g)
p.drawMaskAreas(g)

dwg.add(g)

dwg.save(pretty=True)
