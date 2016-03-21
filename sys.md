
# sys

### What it is good for?

Settings of the Python interpreter itself.

The `sys` module provides an access point to the Python environment. You find there command line arguments, the import path settings, the standard input, output and error stream and many more.

### Installed with Python by default

yes

### Example

Command line parameters used when calling Python:

    >>> import sys
    >>> sys.argv
    ['']

Version of the Python interpreter:

    >>> sys.version
    '3.4.0 (default, Jun 19 2015, 14:20:21) \n[GCC 4.8.2]'

Directories in which Python looks for modules:

    >>> sys.path
    ['', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', 
    '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/site-packages']

Exit Python altogether:

    >>> sys.exit()
    krother@academis:~$

### Where to learn more?

[https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
