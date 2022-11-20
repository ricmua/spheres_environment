""" Data structures and methods for describing and manipulating 
    spherical objects in a 3D virtual environment.

Examples
--------

Initialize an environment instance.

>>> environment = Environment()

Add a pair of spheres to the environment.

>>> sphere_a = environment.initialize_object('sphere_a')
>>> sphere_b = environment.initialize_object('sphere_b')

Verify that the spheres overlap, given the default property values.

>>> def spheres_are_overlapping():
...     p_a = sphere_a.position
...     p_b = sphere_b.position
...     d = sum([(p_b[k] - p_a[k])**2 for k in ['x', 'y', 'z']])
...     return d <= (sphere_a.radius + sphere_b.radius)**2
>>> spheres_are_overlapping()
True

Change the position of `sphere_b` and verify that it still overlaps 
with `sphere_a`.

>>> sphere_b.position = (1, 1, 1)
>>> spheres_are_overlapping()
True

Decrease the radius of `sphere_a` and confirm that the two spheres no 
longer overlap.

>>> sphere_a.radius = 0.1
>>> spheres_are_overlapping()
False

At its core, the environment and all objects in the environment are 
structured as Python mapping data types. The current state of the 
environment can be represented, completely, by converting all objects 
in the environment into dict records.

>>> records = [o.data for o in environment.values()]
>>> import pprint
>>> pprint.pp(records)
[{'position/x': 0.0,
  'position/y': 0.0,
  'position/z': 0.0,
  'radius': 0.1,
  'key': 'sphere_a'},
 {'position/x': 1.0,
  'position/y': 1.0,
  'position/z': 1.0,
  'radius': 1.0,
  'key': 'sphere_b'}]

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Local imports.
from .sphere import Sphere
from .environment import Environment


# Main.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

