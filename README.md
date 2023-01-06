---
title: Spheres environment
author: a.whit ([email](mailto:nml@whit.contact))
date: November 2022
---

<!-- License

Copyright 2022 Neuromechatronics Lab, Carnegie Mellon University (a.whit)

Created by: a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
-->

# Spheres virtual environment

This Python package provides a framework for a virtual environment in which 
spherical objects interact in a 3D space. This is primarily intended for use in 
the development of behavioral tasks for experimental science.

## Installation

The package can be used as-is, so long as the [Python path] is set 
appropriately.
                 
However, `pyoproject.toml` and `setup.cfg` files have been provided, to 
facilitate package installation via [setuptools]. Package installation can be 
accomplished via the [pip install] command:

```
pip install path/to/spheres_environment
```

The update, user, and editable / development flags are common options that can 
be added to the command:

```
pip install -e -U --user path/to/spheres_environment
```

### Testing

Forthcoming.

## Example

Initialize an environment instance.

```python
>>> import spheres_environment
>>> environment = spheres_environment.Environment()

```

Add a pair of spheres to the environment.

```python
>>> sphere_a = environment.initialize_object('sphere_a')
>>> sphere_b = environment.initialize_object('sphere_b')

```

Set the sphere [RGBA] colors.

```python
>>> sphere_a.color = (0.0, 1.0, 0.0, 1.0)
>>> sphere_b.color = (0.0, 0.0, 1.0, 1.0)

```

Verify that the spheres overlap, given the default property values.

```python
>>> def spheres_are_overlapping():
...     p_a = sphere_a.position
...     p_b = sphere_b.position
...     d = sum([(p_b[k] - p_a[k])**2 for k in ['x', 'y', 'z']])
...     return d <= (sphere_a.radius + sphere_b.radius)**2
>>> spheres_are_overlapping()
True

```

Change the position of `sphere_b` and verify that it still overlaps 
with `sphere_a`.

```python
>>> sphere_b.position = (1, 1, 1)
>>> spheres_are_overlapping()
True

```

Decrease the radius of `sphere_a` and confirm that the two spheres no 
longer overlap.

```python
>>> sphere_a.radius = 0.1
>>> spheres_are_overlapping()
False

```

At its core, the environment and all objects in the environment are 
structured as Python mapping data types. The current state of the 
environment can be represented, completely, by converting all objects 
in the environment into dict records.

```python
>>> records = [o.data for o in environment.values()]
>>> import pprint
>>> pprint.pp(records)
[{'color/r': 0.0,
  'color/g': 1.0,
  'color/b': 0.0,
  'color/a': 1.0,
  'position/x': 0.0,
  'position/y': 0.0,
  'position/z': 0.0,
  'radius': 0.1,
  'key': 'sphere_a'},
 {'color/r': 0.0,
  'color/g': 0.0,
  'color/b': 1.0,
  'color/a': 1.0,
  'position/x': 1.0,
  'position/y': 1.0,
  'position/z': 1.0,
  'radius': 1.0,
  'key': 'sphere_b'}]

```

## License

Copyright 2022 [Neuromechatronics Lab][neuromechatronics], 
Carnegie Mellon University

Contributors: 

* a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.

<!---------------------------------------------------------------------
   References
---------------------------------------------------------------------->

[Python path]: https://docs.python.org/3/tutorial/modules.html#the-module-search-path

[doctest]: https://docs.python.org/3/library/doctest.html

[rewarding outcome]: https://en.wikipedia.org/wiki/Reinforcement

[neural codes]: https://en.wikipedia.org/wiki/Neuronal_ensemble#Background

[motor cortex]: https://en.wikipedia.org/wiki/Primary_motor_cortex#Movement_coding

[center-out task]: https://pubmed.ncbi.nlm.nih.gov/3411362/

[pytransitions]: https://github.com/pytransitions/transitions

[doctest]: https://docs.python.org/3/library/doctest.html

[ros_transitions]: https://github.com/ricmua/ros_transitions

[separation of concerns]: https://en.wikipedia.org/wiki/Separation_of_concerns

[ros_force_dimension]: https://github.com/ricmua/ros_force_dimension

[ROS2]: https://docs.ros.org/en/humble/index.html

[Unity3D]: https://en.wikipedia.org/wiki/Unity_(game_engine)

[unity_spheres_environment]: https://github.com/ricmua/unity_spheres_environment

[setuptools]: https://setuptools.pypa.io/en/latest/userguide/quickstart.html#basic-use

[neuromechatronics]: https://www.meche.engineering.cmu.edu/faculty/neuromechatronics-lab.html

[pip install]: https://pip.pypa.io/en/stable/cli/pip_install/

[pytest]: https://docs.pytest.org/

[unittest]: https://docs.python.org/3/library/unittest.html

[RGBA]: https://en.wikipedia.org/wiki/RGBA_color_model

