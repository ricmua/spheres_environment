""" Base classes for a generic virtual environment.

The virtual environment defines rules and data structures that 
represent the interaction among objects in the environment. The 
`Environment` class consists of a mapping between object keys and 
collections of object properties.

Examples
--------

Initialize a virtual environment.

>>> environment = Environment()

Create a derivative of the `Object` class that maintains a `position` 
property, in order to represent some object that is situated at a 
particular location in some virtual 3D space.

>>> class SituatedObject(Object):
...     @object_property
...     def position(self):
...         default = dict(x=0.0, y=0.0, z=0.0)
...         position = self.setdefault('position', default)
...         position = {k: float(position[k]) for k in ['x', 'y', 'z']}
...         return position

Add the new object class to the environment schema -- or the collection 
of objects that the environment recognizes.

>>> environment.object_type_map.update(situated_object=SituatedObject)

Initialize an object with the default object type.

>>> object_a = environment.initialize_object('object_a')

Initialize an object with the "situated object" type.

>>> object_b = environment.initialize_object('object_b', 'situated_object')

The initialized objects are part of the environment data structure, but 
uninitialized objects are not recognized.

>>> 'object_a' in environment
True
>>> 'object_b' in environment
True
>>> 'object_c' in environment
False

The situated object (`object_b`) has a `position` property, but the 
other object (`object_a`) does not.

>>> object_a.is_object_property('position')
False
>>> object_b.is_object_property('position')
True
>>> object_b.object_properties
['position']

The situated object is characterized by the `position` property, 
which consists of a dict of three floats. Test the position property 
for `object_b`.

>>> object_b.position
{'x': 0.0, 'y': 0.0, 'z': 0.0}
>>> object_b['position'] = dict(x=1, y=2, z=3)
>>> tuple(object_b.position.values())
(1.0, 2.0, 3.0)

The environment consists of all objects and their properties.

>>> environment
{'object_a': {}, 'object_b': {'position': {'x': 1, 'y': 2, 'z': 3}}}

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Local imports.
from spheres_environment.object import object_property
from spheres_environment.object import Object


# Environment class.
class Environment(dict):
    """ Defines rules and data structures representing the interaction 
        among objects in a virtual environment.
    
    Fundamentally, this class consists of a mapping between unique 
    object keys and object instances (which can themselves be reduced 
    to object properties and the methods that operate on those 
    properties). Methods can be added to derivative classes in order 
    to operate on, and define interactions between, the objects in the 
    environment.
    """
     
    object_type_map = dict(object=Object)
    """ Mapping between object type keys and the object classes that 
        they correspond to.
    """
    
    def initialize_object(self, key, type_key=None, **kwargs):
        """ Initialize a new object in the environment.
        
        Although objects can be initialized directly using the mapping 
        or `__setitem__` accessor, it is better to initialize objects 
        functionally. This ensures that object classes are of a 
        recognized type, and performs any needed housekeeping.
        
        Arguments
        ---------
        key : str
            Unique key used to identify an object in the environment.
        type_key : str
            Unique key that references an item in the `object_type_map` 
            class variable. Defines the type of the initialized object. 
            Defaults to the first key in the mapping, if not specified.
        
        Returns
        -------
        object
            The initialized object instance.
        """
        default_key = next(iter(self.object_type_map))
        type_key = type_key if type_key else default_key
        object_class = self.object_type_map[type_key]
        self[key] = object_class(key=key, **kwargs)
        return self[key]
        
    def destroy_object(self, key):
        """ Remove an object from the environment. """
        del self[key]
        
    def set_property(self, object_key, property_key, **kwargs):
        """ Set the value of an object property.
        
        Arguments
        ---------
        object_key : str
            Object key that identifies the object in the environment for which 
            a property value is to be set.
        property_key : str
            Property key that identifies the property for which a value is to 
            be set.
        **kwargs : dict
            Keyword arguments corresponding to the fields of the property to be 
            set. For scalar properties, use `value` as the key.
        """
        value = kwargs['value'] if (list(kwargs) == ['value']) else kwargs
        setattr(self[object_key], property_key, value)
   
 

# Main.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

