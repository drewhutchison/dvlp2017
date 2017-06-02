import svgwrite

from components import *

class Cluster(object):

    def addExclusions(self, addable):
        for c in self.components:
            addable.add(c.excludedElement)

    def addBoundBox(self, addable):
        g = svgwrite.container.Group(class_=self.__class__.__name__)
        g.add(self.bbox)
        addable.add(g)

    addBoundboxes = addBoundBox

class SpdtCluster(Cluster):
    '''this should originate from the bottom left-hand corner of the 
    bottommost jack's padded area'''

    hpad = 50
    vpad = 100

    height = Jack.r_exclude * 8 + vpad * 3
    width = Jack.r_exclude * 2

    def __init__(self, x, y, name='unnamed'):

        v_centerline = x + Jack.r_exclude
        h_baseline = y

        self.components = [
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude,
                name+'.NC'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NO'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.COM'),
            Jack(v_centerline, 
                h_baseline - Jack.r_exclude * 7 - self.vpad * 3,
                name+'.COIL')
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (Jack.r_exclude * 2, self.height))

class DpdtCluster(Cluster):

    hpad = 100
    vpad = 100

    # TODO top element spacing might change
    height = Jack.r_exclude * 8 + vpad * 3
    width = Jack.r_exclude * 4 + hpad

    def __init__(self, x, y, name='unnamed'):

        v_centerline1 = x + Jack.r_exclude
        v_centerline2 = x + Jack.r_exclude * 3 + self.hpad
        h_baseline = y

        self.components = [
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude,
                name+'.NC1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NO1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.COM1'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude,
                name+'.NC2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NO2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.COM2'),
            Jack((v_centerline1 + v_centerline2)/2,
                h_baseline - Jack.r_exclude * 7 - self.vpad * 3)
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (Jack.r_exclude * 4 + self.hpad, self.height))
        
class DpdtInvertedCluster(Cluster):

    hpad = 100
    vpad = 100

    # TODO top element spacing might change
    height = Jack.r_exclude * 8 + vpad * 3
    width = Jack.r_exclude * 4 + hpad

    def __init__(self, x, y, name='unnamed'):

        v_centerline1 = x + Jack.r_exclude
        v_centerline2 = x + Jack.r_exclude * 3 + self.hpad
        h_baseline = y

        self.components = [
            Jack((v_centerline1 + v_centerline2)/2,
                h_baseline - Jack.r_exclude,
                name+'COIL'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NC1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.NO1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 7 - self.vpad * 3,
                name+'.COM1'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 3 - self.vpad,
                name+'.NC2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 2,
                name+'.NO2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 7 - self.vpad * 3,
                name+'.COM2'),
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (Jack.r_exclude * 4 + self.hpad, self.height))
        
class McCluster(Cluster):

    width = 2000
    height = 4000

    def __init__(self, x, y):

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (self.width, self.height)
        )

    def addExclusions(self, addable):
        return self.addBoundBox(addable)
