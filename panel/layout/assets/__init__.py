
import svgwrite

import superclusters 

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

    def addSpdtSupercluster(self, x, y, N=None):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.SpdtSupercluster(self.X + x, self.Y - y, N))

    def addDpdtSupercluster(self, x, y, N=None):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.DpdtSupercluster(self.X + x, self.Y - y, N))

    def addInvertedDpdtSupercluster(self, x, y, N=None):
        '''
        x and y relative llh panel corner, y upward
        '''
        self.clusters.append(superclusters.DpdtInvertedSupercluster(self.X + x, self.Y - y, N))

    def addMC(self, x, y):
        self.clusters.append(superclusters.McCluster(self.X + x, self.Y - y))

    def drawExclusionAreas(self, addable):
        for cluster in self.clusters:
            cluster.addExclusions(addable)
    
    def drawBoundboxes(self, addable):
        for cluster in self.clusters:
            cluster.addBoundboxes(addable)
    
__all__ = [
    'Panel'
]
