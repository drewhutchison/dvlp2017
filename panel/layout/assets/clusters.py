import svgwrite

from components import *

class Cluster(object):

    def __str__(self):
        return ('\n{} composed of:\n\n\t' +
                '\n\t'.join([str(component) for component in self.components])
                ).format(self.__class__.__name__)

    def addExclusions(self, addable):
        for c in self.components:
            addable.add(c.excludedElement)

    def addMasks(self, addable):
        for c in self.components:
            addable.add(c.maskedElement)

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
    keyswitch_pad = 40

    def __init__(self, x, y):
        v_centerline = x + self.width/2

        self.components = [
            Fuse(v_centerline, y - Fuse.r_exclude),
            Lamp(v_centerline, y - Fuse.r_exclude*2 - self.vpad - Lamp.r_exclude, "pilot"),
            Keyswitch(v_centerline, y - Fuse.r_exclude*2 - self.vpad*2 - Lamp.r_exclude*2 - Keyswitch.r_exclude - self.keyswitch_pad, "power")
        ]

        self.bbox = shapes.Rect(
            (x, y-self.height),
            (self.width, self.height)
        )

##    def addExclusions(self, addable):
##        return self.addBoundBox(addable)

class SwitchCluster(Cluster):

    vpad = 100
    switch_pad = 3
    
    width = Jack.r_exclude * 2
    height = Jack.r_exclude * 6 + Switch.height + vpad*3

    def __init__(self, x, y, name='unnamed'):
        v_centerline = x + Jack.r_exclude

        self.components = [
            Jack(v_centerline, y - Jack.r_exclude, name + '.NC'),
            Jack(v_centerline, y - Jack.r_exclude*3 - self.vpad, name + '.NO'),
            Jack(v_centerline, y - Jack.r_exclude*5 - self.vpad*2, name + '.COM'),
            Switch(v_centerline,
                   y - Jack.r_exclude*6 - self.vpad*3 - Switch.height/2 - self.switch_pad, name)
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

class VTiepointCluster(Cluster):

    vpad = 100

    def __init__(self, x, y, name):

        v_centerline = x + Jack.r_exclude

        self.components = [
            Jack(v_centerline, y + Jack.r_exclude),
            Jack(v_centerline, y + Jack.r_exclude*3 + self.vpad)
        ]

class LampCluster(Cluster):

    vpad = 100
    jack_hoffs = 0
    jack_voffs = 0

    height = Lamp.r_exclude * 2 + Jack.r_exclude * 2 + vpad
    width = 2*Lamp.r_exclude

    def __init__(self, x, y, name):

        v_centerline = x + Lamp.r_exclude

        self.components = [
            Lamp(v_centerline, y - Jack.r_exclude*2 - self.vpad - Lamp.r_exclude),
            Jack(v_centerline - self.jack_hoffs, y - Jack.r_exclude -
                self.jack_voffs)
        ]

        self.bbox = shapes.Rect(
            (x, y - self.height),
            (Lamp.r_exclude*2, self.height)
        )
