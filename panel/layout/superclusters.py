from clusters import *

class SpdtSuperCluster(object):

    def __init__(self, x, y):
        self.clusters = [
                SpdtCluster(x + (i*1000), y)
                for i in range (8)
                ]

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

