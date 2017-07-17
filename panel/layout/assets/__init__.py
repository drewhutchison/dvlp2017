
import svgwrite

import superclusters 

class Panel(object):

    # hardcoded lower-left-hand-corner origin in user coords
    X = 1000
    Y = 9000

    # rectangle css style
    STYLE = '''
        fill: none;
        stroke: black;
        stroke-width: 15px;
        '''
    
    superclusters.set_panel_offset(X, Y)

    # hardcoded width figures
    fullwidth = 19000
    inclusionwidth = 17500

    # nominal height in rack units
    nU = 4

    # allow 1/32in slop
    height = 1750 * nU - 31

    def __init__(self):
        self.clusters = []

    def __str__(self):
        return ('Panel composed of: \n\t' +
                '\n\t'.join([str(cluster) for cluster in self.clusters]))

    def drawFrame(self, addable):
        addable.add(svgwrite.shapes.Rect(
            (self.X, self.Y-self.height), 
            (self.fullwidth, self.height),
            class_='frame',
            style=self.STYLE))
        addable.add(svgwrite.shapes.Rect(
            (self.X + (self.fullwidth-self.inclusionwidth)/2,
                self.Y-self.height), 
            (self.inclusionwidth, self.height),
            class_='frame',
            style=self.STYLE))

    def addSpdtSupercluster(self, x, y, N=None):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.SpdtSupercluster(self.X + x, self.Y - y, N))

    def addDpdtSupercluster(self, x, y, N=None, start=1, label='R'):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.DpdtSupercluster(self.X + x,
            self.Y - y,
            N,
            start=start,
            label=label))

    def addInvertedDpdtSupercluster(self, x, y, N=None):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.DpdtInvertedSupercluster(self.X + x, self.Y - y, N))

    def addMC(self, x, y):
        self.clusters.append(superclusters.McCluster(self.X + x, self.Y - y))

    def addSwitchSupercluster(self, x, y, N=None):
        self.clusters.append(superclusters.SwitchSupercluster(self.X + x, self.Y - y))

    def addHTiepointCluster(self, x, y, name="unnamed"):
        self.clusters.append(clusters.HTiepointCluster(self.X + x, self.Y - y, name))

    def addVTiepointCluster(self, x, y, name="unnamed"):
        self.clusters.append(clusters.VTiepointCluster(self.X + x, self.Y - y, name))

    def addLampSupercluster(self, x, y, name="unnamed"):
        self.clusters.append(superclusters.LampSupercluster(self.X + x, self.Y - y))

    def drawExclusionAreas(self, addable):
        for cluster in self.clusters:
            cluster.addExclusions(addable)

    def drawMaskAreas(self, addable):
        for cluster in self.clusters:
            cluster.addMasks(addable)
    
    def drawBoundboxes(self, addable):
        for cluster in self.clusters:
            cluster.addBoundboxes(addable)

    def drawLabels(self, addable):
        for cluster in self.clusters:
            cluster.addLabels(addable)
    
__all__ = [
    'Panel'
]
