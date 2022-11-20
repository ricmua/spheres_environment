""" Base class for a generic object in an environment.

Defines the data structures and methods for recording and manipulating 
the properties of an object in a virtual environment.

Examples
--------

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

Initialize an object with the default object type.

>>> object_a = Object('object_a')

Initialize an object with the "situated object" type.

>>> object_b = SituatedObject('object_b')

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

Object data is easily converted to a neat records format.

>>> object_b.data
{'position/x': 1.0, 'position/y': 2.0, 'position/z': 3.0, 'key': 'object_b'}

"""

# Copyright 2022 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Import collections abstract base classes.
import collections.abc


# Object properties.
class object_property(property):
    """ A property of an object in a virtual environment.
    
    Object properties are distinguished from general Python properties 
    in order to facilitate convenient type checking.
    """
    pass
        
  

class Object(dict):
    """ Base class for all objects contained in an environment.
    
    Arguments
    ---------
    key : str
        A unique key used to identify an object in the environment.
    """
    def __init__(self, key, **kwargs):
        """
        """
        self._key = key
        super().__init__(**kwargs)
        
    @property
    def key(self):
        """ A unique key used to identify an object in the 
            environment.
        """
        return self._key
    
    @property
    def object_properties(self):
        """ A list of keys for all object properties. """
        attributes = dir(self)
        attributes.remove('object_properties')
        is_object_property = lambda o: isinstance(o, object_property)
        return [k for k in attributes 
                if is_object_property(getattr(self.__class__, k, {}))]
    
    def is_object_property(self, key):
        """ Tests where or not a provided key maps to a property that 
            has been defined for this object.
        """
        return key in self.object_properties
        
    @property
    def data(self):
        """ State of the object in neat record format. """
        return self.to_record(delimiter='/')
        
    def to_record(self, delimiter='_'):
        """ Convert object data to a neat record format. """
        
        # Define a conversion for string or numeric types.
        from_scalar = lambda k,v: {k: v}
        
        # Define a conversion for sequence types.
        from_sequence \
          = lambda k,v: {f'{k}{delimiter}{i}': vi for (i, vi) in enumerate(v)}
        
        # Define a conversion for mapping types.
        from_mapping \
          = lambda k,v: {f'{k}{delimiter}{ki}': vi for (ki, vi) in v.items()}
        
        ## Not found case.
        #not_found = lambda k,v: raise Exception()
        
        # Define a conversion mapping.
        convert_mapping \
          = {int: from_scalar, 
             float: from_scalar, 
             str: from_scalar,
             tuple: from_sequence,
             list: from_sequence,
             dict: from_mapping,
            }
        get_type = lambda k: type(getattr(self, k))
        convert = lambda k: convert_mapping[get_type(k)](k, getattr(self, k))
        
        # Convert the object properties into the desire data format.
        record = {ki: vi 
                  for k in self.object_properties
                  for (ki, vi) in convert(k).items()
                 }
        
        # Add the object key to the record.
        record['key'] = self.key
        
        # Return the result.
        return record
    
    #def __getitem__(self, key):
    #    """
    #    """
    #    #if key not in self.object_properties: raise Exception
    #    return super().__getitem__(key)
    #    
    #def __setitem__(self, key, value):
    #    """
    #    """
    #    #if key not in self.object_properties: raise Exception
    #    super().__setitem__(key, value)
    
  

# Main.
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

