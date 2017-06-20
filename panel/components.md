This file describes the panel-mount components.

# Terminology

_Exclusion area_ is the area physically occupied by the component body.
No components may overlap with regard to exclusion area.

_Mask area_ is the area masked by the component's front-side mounting hardware.
No important graphics should exist in the mask area.
Mask area is taken in elevation only, and does not account for parallax.

_Knockout area_ respresents the material physically removed from the panel to 
accomodate the component's pass-through.

# Connectors

Patch connections are made over 1/4" TS phone jacks, of which only the tip 
connection is used.
Switch and relay common terminals are normalized to +12V.
Two 4-way tiepoint connections are provided, which are normalized to +12V and 
0V, respectively.
All other connections are non-normalized.

- Normalized connectors are Switchcraft 12A.
- Non-normalized connectors are Neutrik NYS229.

Connector dimensions are comparable for both, and rounded up to:

- Exclusion area is a cicle of diameter .770".
  This neglects terminal overlap, which is assumed to be corrected by manual
  rotation of components.
- Mask area is a circle of diameter .591".
- Knockout area is a circle of diameter .394".

# Switches

Switches are ON-(ON) SPDT momentary miniature toggle type.
These are NKK part no. M2015SS1W01.

- Exclusion area is the switch body, a rectangle .512 x .311"
  This neglects the lock and keyway washers which overhang slightly.
- Mask area is the .364" bounding circle of the nut.
- Cutout area is .250" for the mount bushing.
  This will include a keyway if the fabricator allows.

# Lamps

Indicator lamps are accomodated in lamp holder, Dialight part no.
095-0408-09-172.

- Exlusion area represents the back-side internally toothed lockwasher, 
  nominal diameter 61/64", rounded to .960".
- Mask area is the front-side mounting flange, nominal diameter 13/16", 
  taken to be .813".
- Knockout area is a circle of diameter .682".

# Keyswitch

Master system power is controlled by a keyswitch, CIC Components part no. 
196649.
Their website sucks, but [Jameco](http://www.jameco.com/) carries it as the
same part no.

- The knockout area is an M19 (.748") circle, neglecting the keying.
- The mask area is the M22 (.868") diameter of the lock body mounting flange.
- The exclusion area is the 1.081" diameter of the conical mounting 
  springwasher/fairing.

# Fuse holder

The system master fuse is mounted on the panel and held in a standard
panel-mount fuseholder (Jameco part no. 18703).
The mask and knockout areas are identical to those of the connectors, and the
former defines the exclusion area.

- The knockout area is a circle of diameter .510", neglecting the keying
- The mask and exclusion areas are defined by the bounding circle of the
  front-side nut, .760" diameter.

