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

Forthcoming.

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

