from clusters import *

class Supercluster(object):

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

    def addBoundboxes(self, addable):

        addable.add(self.bbox)

        for c in self.clusters:
            c.addBoundBox(addable)

class SpdtSupercluster(Supercluster):

    hpad = 100

    N = 8

    def __init__(self, x, y):
        self.clusters = [
                SpdtCluster(x + (i*(SpdtCluster.width+self.hpad)), y)
                for i in range (self.N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (self.N * SpdtCluster.width + (self.N - 1) * self.hpad, 
                SpdtCluster.height)
        )

class DpdtSupercluster(Supercluster):

    hpad = 100

    N = 4

    def __init__(self, x, y):
        self.clusters = [
            DpdtCluster(x + (i*(DpdtCluster.width+self.hpad)), y)
            for i in range(self.N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (self.N * SpdtCluster.width + (self.N - 1) * self.hpad, 
                SpdtCluster.height)
        )

