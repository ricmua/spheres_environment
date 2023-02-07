""" Data structure and methods for recording and manipulating the 
    properties of 3D spherical objects.

Examples
--------

Initialize a sphere with default property values.

>>> sphere = Sphere('sphere')
>>> sphere
{}

Get the default property values.

>>> sphere.position
{'x': 0.0, 'y': 0.0, 'z': 0.0}
>>> sphere.radius
1.0

Set new property values.

>>> sphere.position = (1, 2, 3)
>>> sphere.radius = 2
>>> sphere
{'position': {'x': 1.0, 'y': 2.0, 'z': 3.0}, 'radius': 2.0}

Retrieve the sphere data in records format.

>>> import pprint
>>> pprint.pp(sphere.data)
{'position/x': 1.0,
 'position/y': 2.0,
 'position/z': 3.0,
 'radius': 2.0,
 'key': 'sphere'}

Test whether or not the sphere intersects with other spheres centered at the 
origin.

>>> sphere.intersects(Sphere('other'))
False
>>> sphere.intersects(Sphere('other', position=dict(x=0.0, y=2.0, z=3.0)))
True
>>> sphere.intersects(Sphere('other', radius=15))
True


"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Import collection abstract base classes.
import collections.abc

# Import numpy.
import numpy
from numpy import linalg

# Local imports.
from spheres_environment import base


# Sphere class.
class Sphere(base.Object):
    """ A situated, volumetric, spherical object. """
    
    TYPE='sphere'
    
    @base.object_property
    def position(self):
        """ Position of the sphere in 3D space. """
        default = dict(x=0.0, y=0.0, z=0.0)
        position = self.setdefault('position', default)
        position = {k: float(position[k]) for k in ['x', 'y', 'z']}
        return position
        
    @position.setter
    def position(self, value):
        keys = ['x', 'y', 'z']
        if isinstance(value, tuple): value = dict(zip(keys, value))
        self['position'] = {k: float(v) for (k, v) in value.items()}
    
    @base.object_property
    def radius(self):
        """ Radius of the sphere. """
        radius = self.setdefault('radius', 1.0)
        return float(radius)
    
    @radius.setter
    def radius(self, value):
        value = value['value'] if isinstance(value, dict) else value
        assert not isinstance(value, collections.abc.Collection)
        self['radius'] = float(value)
        
    def intersects(self, other):
        """ Test whether or not this sphere intersects with another.
        
        Parameters
        ----------
        other : Sphere
            A Sphere to compare against.
        
        Returns
        -------
        intersects : bool
            True if the spheres intersect.
        """
        # Compute the distance between the sphere center and the point.
        p_s = tuple(self.position[k] for k in ('x', 'y', 'z'))
        p_o = tuple(other.position[k] for k in ('x', 'y', 'z'))
        d = numpy.array(p_s) - p_o
        m = numpy.sqrt((d**2).sum())
        
        # Test whether or not any point lies within the sphere.
        return (m <= self.radius + other.radius)

        
    #def __str__(self):
    #    from pprint import pformat
    #    return pformat(self, indent=1)

    
  

# Main.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

