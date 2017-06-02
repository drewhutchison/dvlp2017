from clusters import *

class Supercluster(object):

    defaultN = 8

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

    def addBoundboxes(self, addable):

        addable.add(self.bbox)

        for c in self.clusters:
            c.addBoundBox(addable)

class SpdtSupercluster(Supercluster):

    hpad = 100

    def __init__(self, x, y, N=None):
        N = N if N else self.defaultN
        self.clusters = [
                SpdtCluster(x + (i*(SpdtCluster.width+self.hpad)), y)
                for i in range (N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (N * SpdtCluster.width + (N - 1) * self.hpad, 
                SpdtCluster.height)
        )

class DpdtSupercluster(Supercluster):

    hpad = 100

    def __init__(self, x, y, N=None):
        N = N if N else self.defaultN
        self.clusters = [
            DpdtCluster(x + (i*(DpdtCluster.width+self.hpad)), y)
            for i in range(N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (N * SpdtCluster.width + (N - 1) * self.hpad, 
                SpdtCluster.height)
        )

class DpdtInvertedSupercluster(Supercluster):

    hpad = 100

    def __init__(self, x, y, N=None):
        N = N if N else self.defaultN
        self.clusters = [
            DpdtInvertedCluster(x + (i*(DpdtCluster.width+self.hpad)), y)
            for i in range(N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (N * SpdtCluster.width + (N - 1) * self.hpad, 
                SpdtCluster.height)
        )

