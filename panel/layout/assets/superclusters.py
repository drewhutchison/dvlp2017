from clusters import *

def set_panel_offset(x, y):
    Component.panel_offset_x = x
    Component.panel_offset_y = y

class Supercluster(object):

    defaultN = 8

    def __str__(self):
        return ('\n{} composed of\n' +
                '\n\t'.join([str(cluster) for cluster in self.clusters])
                ).format(self.__class__.__name__)

    def addExclusions(self, addable):
        for c in self.clusters:
            c.addExclusions(addable)

    def addMasks(self, addable):
        for c in self.clusters:
            c.addMasks(addable)

    def addBoundboxes(self, addable):

        addable.add(self.bbox)

        for c in self.clusters:
            c.addBoundBox(addable)

    def addLabels(self, addable):
        for c in self.clusters:
            c.addLabels(addable)

class SpdtSupercluster(Supercluster):

    hpad = 120

    def __init__(self, x, y, N=None, start=1):
        N = N if N else self.defaultN
        self.clusters = [
                SpdtCluster(x + (i*(SpdtCluster.width+self.hpad)),
                    y,
                    'R{}'.format(start + i))
                for i in range (N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SpdtCluster.height),
            (N * SpdtCluster.width + (N - 1) * self.hpad, 
                SpdtCluster.height)
        )

class DpdtSupercluster(Supercluster):

    hpad = 180

    def __init__(self, x, y, N=None, start=1, label='R'):
        N = N if N else self.defaultN
        self.clusters = [
            DpdtCluster(x + (i*(DpdtCluster.width+self.hpad)),
                y,
                '{}{}'.format(label, start+i))
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

class SwitchSupercluster(Supercluster):

    hpad = 200

    defaultN = 4

    def __init__(self, x, y, N=None, start=1):
        N = N if N else self.defaultN
        self.clusters = [
            SwitchCluster(x + i*SwitchCluster.width + self.hpad*i,
                y,
                'S{}'.format(start + i))
            for i in range(N)
        ]

        self.bbox = shapes.Rect(
            (x, y-SwitchCluster.height),
            ((N*SwitchCluster.width + (N-1)*self.hpad), SwitchCluster.height)
        )

class LampSupercluster(Supercluster):

    hpad = 250

    defaultN = 4

    def __init__(self, x, y, N=None):
        N = N if N else self.defaultN

        self.clusters = [
            LampCluster(x + i*LampCluster.width + i*self.hpad, y, 'unnamed')
            for i in range(N)
        ]

        self.bbox = shapes.Rect(
            (x, y-LampCluster.height),
            (N*LampCluster.width + (N-1)*self.hpad, LampCluster.height)
        )
