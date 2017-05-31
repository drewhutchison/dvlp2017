from clusters import *

class Supercluster(object):

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

class SpdtSuperCluster(Supercluster):

    hpad = 1000

    def __init__(self, x, y):
        self.clusters = [
                SpdtCluster(x + (i*self.hpad), y)
                for i in range (8)
        ]

class DpdtSupercluster(Supercluster):

    hpad = 2000

    def __init__(self, x, y):
        self.clusters = [
            DpdtCluster(x + (i*self.hpad), y)
            for i in range(4)
        ]
