from components import *

class SpdtCluster(object):
    '''this should originate from the bottom left-hand corner of the 
    bottommost jack's padded area'''

    hpad = 50
    vpad = 100

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

    def addExclusions(self, addable):
        for c in self.components:
            addable.add(c.excludedElement)

    def addBoundBox(self, addable):
        addable.add(self.bbox)

