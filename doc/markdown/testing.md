<!-- License

Copyright 2023 Neuromechatronics Lab, Carnegie Mellon University (a.whit)

Contributors:
  a. whit. (nml@whit.contact)

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at https://mozilla.org/MPL/2.0/.
-->

## Testing

Unit, integration, and/or regression tests are included in this package.

### doctest

Tests written into the documentation can be invoked via the [doctest] package 
and testing framework. This is a **recommended first step**, to ensure basic 
functionality. Doctests are included in many of the Python source code files, 
as well as the package README and some of the Markdown documentation files.

```bash
python -m doctest path/to/spheres_environment/README.md
```

The following doctest commands are valid (assuming invocation from the 
package root):

* `python -m doctest README.md`
* `python -m doctest spheres_environment/base.py`
* `python -m doctest spheres_environment/environment.py`
* `python -m doctest spheres_environment/history.py`
* ~~`python -m doctest spheres_environment/__init___.py`~~ (_See below_)

If desired, the doctests can also be run directly from a Python environment.

```python
import doctest
doctest.testfile('path/to/README.md', module_relative=False)
```

This approach is useful for running the doctests in the package `__init__.py` 
file.

```python
import doctest
import spheres_environment
doctest.testmod(spheres_environment)
```

All tests should complete without reporting errors.

### pytest

At present, no [pytest]-based tests are available for this package.


<!---------------------------------------------------------------------
   References
---------------------------------------------------------------------->

[Python path]: https://docs.python.org/3/tutorial/modules.html#the-module-search-path

[doctest]: https://docs.python.org/3/library/doctest.html

[pytest]: https://docs.pytest.org/

[pytest keyword expression]: https://docs.pytest.org/en/7.2.x/how-to/usage.html#specifying-which-tests-to-run


