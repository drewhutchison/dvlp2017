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
    vpad_iso = hpad * .866

    # TODO top element spacing might change
    height = Jack.r_exclude * 8 + vpad * 2 + vpad_iso
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
                h_baseline - Jack.r_exclude * 7 - self.vpad * 2)
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (Jack.r_exclude * 4 + self.hpad, self.height))
        
class DpdtInvertedCluster(DpdtCluster):

##    hpad = 100
##    vpad = 100
##
##    # TODO top element spacing might change
##    height = Jack.r_exclude * 8 + vpad * 3
##    width = Jack.r_exclude * 4 + hpad

    def __init__(self, x, y, name='unnamed'):

        v_centerline1 = x + Jack.r_exclude
        v_centerline2 = x + Jack.r_exclude * 3 + self.hpad
        h_baseline = y

        self.components = [
            Jack((v_centerline1 + v_centerline2)/2,
                h_baseline - Jack.r_exclude,
                name+'COIL'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 3 - self.vpad_iso,
                name+'.NC1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 1 - self.vpad_iso,
                name+'.NO1'),
            Jack(v_centerline1,
                h_baseline - Jack.r_exclude * 7 - self.vpad * 2 - self.vpad_iso,
                name+'.COM1'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 3 - self.vpad_iso,
                name+'.NC2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 5 - self.vpad * 1 - self.vpad_iso,
                name+'.NO2'),
            Jack(v_centerline2,
                h_baseline - Jack.r_exclude * 7 - self.vpad * 2 - self.vpad_iso,
                name+'.COM2'),
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (Jack.r_exclude * 4 + self.hpad, self.height))
        
class McCluster(Cluster):

    width = 2000
    height = 3000

    vpad = 100

    def __init__(self, x, y):

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (self.width, self.height)
        )

    def addExclusions(self, addable):
        return self.addBoundBox(addable)

class SwitchCluster(Cluster):

    vpad = 100
    
    width = Jack.r_exclude * 2
    height = Jack.r_exclude * 6 + Switch.height + vpad*3

    def __init__(self, x, y, name='unnamed'):
        v_centerline = x + Jack.r_exclude

        self.components = [
            Jack(v_centerline, y - Jack.r_exclude, name + '.NC'),
            Jack(v_centerline, y - Jack.r_exclude*3 - self.vpad, name + '.NO'),
            Jack(v_centerline, y - Jack.r_exclude*5 - self.vpad*2, name + '.COM'),
            Switch(v_centerline,
                   y - Jack.r_exclude*6 - self.vpad*4 - Switch.height/2, name)
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (self.width, self.height))

class HTiepointCluster(Cluster):

    hpad = 100

    def __init__(self, x, y, name):

        h_centerline = y - Jack.r_exclude

        self.components = [
            Jack(x + Jack.r_exclude, h_centerline, name + '.NORM'),
            Jack(x + Jack.r_exclude*3 + self.hpad, h_centerline, name + '.2'),
            Jack(x + Jack.r_exclude*5 + self.hpad*2, h_centerline, name + '.3'),
            Jack(x + Jack.r_exclude*7 + self.hpad*3, h_centerline, name + '.4'),
        ]

        self.bbox = shapes.Rect(
            (x, y - Jack.r_exclude*2),
            (8*Jack.r_exclude + 3*self.hpad, Jack.r_exclude*2)
        )
