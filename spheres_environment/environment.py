""" Data structures and methods for a 3D virtual environment that 
    contains interacting spherical objects.

Examples
--------

Initialize a virtual environment.

>>> environment = Environment()

Add a sphere object to the environment.

>>> sphere = environment.initialize_object('sphere')

Verify the properties of the sphere object.

>>> sphere.object_properties
['position', 'radius']

Change the properties from the default values.

>>> sphere.position = (1, 2, 3)
>>> sphere.radius = 2
>>> sphere
{'position': {'x': 1.0, 'y': 2.0, 'z': 3.0}, 'radius': 2.0}

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Local imports.
from spheres_environment import base
from spheres_environment.sphere import Sphere

# Virtual environment class.
class Environment(base.Environment):
    """ Defines rules and data structures representing the interaction 
        among spheres in a 3D virtual environment.
    """
    object_type_map = dict(sphere=Sphere)
    
    def set_color(self, key, r=0.0, g=0.0, b=0.0, a=1.0):
        self[key].color = dict(r=r, g=g, b=b, a=a)
    
  

# Main.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

