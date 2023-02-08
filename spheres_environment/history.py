""" Functionality for recording object state histories.

Examples
--------

Initialize a buffer for recording the state history for a counter object.

>>> counter = dict(count=0)
>>> history = Buffer(obj=counter, length=3)
>>> list(history)
[{'count': 0}, {'count': 0}, {'count': 0}]

Increment the counter and verify that the most recent element of the history 
buffer is also modified.

>>> counter['count'] += 1
>>> list(history)
[{'count': 0}, {'count': 0}, {'count': 1}]

Update the state history buffer in order to push a copy of the counter state.

>>> history.sample()
>>> list(history)
[{'count': 0}, {'count': 1}, {'count': 1}]

Increment the counter again and verify that the most recent element of the 
history buffer is again modified.

>>> counter['count'] += 1
>>> list(history)
[{'count': 0}, {'count': 1}, {'count': 2}]

Again update the state history buffer and increment.

>>> history.sample()
>>> counter['count'] += 1
>>> list(history)
[{'count': 1}, {'count': 2}, {'count': 3}]

Note that the buffer discards the oldest state, each time it is updated.

"""

# Copyright 2022-2023 Carnegie Mellon University Neuromechatronics Lab (a.whit)
# 
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.
# 
# Contact: a.whit (nml@whit.contact)


# Import copy.
from copy import copy

# Import deque.
from collections import deque


# History buffer class.
class Buffer(deque):
    """ A [deque] (double-ended queue) buffer that stores a history of object  
        states (i.e., snapshots).
        
    [deque]: https://docs.python.org/3/library/collections.html
             #collections.deque
    
    Parameters
    ----------
    
    obj
      An object for which a state history is to be maintained.
    length : int
      Length of the state history buffer. Each time the buffer is updated, the 
      oldest element is discarded.
    
    """
    
    DEFAULT_LENGTH = 2
    """ Default length of the buffer, if not specified explicitly. """
    
    def __init__(self, obj, length=None):
        length = length if length else self.DEFAULT_LENGTH
        iterable = [copy(obj) for n in range(length)]
        super().__init__(iterable=iterable, maxlen=length)
        #self._object=obj
        self.sample(obj=obj)
        
    def sample(self, obj=None):
        """ Push a copy the current object state into the history buffer. """
        self._object = self._object if (obj is None) else obj
        self[-1] = copy(self._object)
        self.rotate(-1)
        self[-1] = self._object
    
  

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
  

