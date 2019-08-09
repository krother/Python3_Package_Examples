
# sys

### What it is good for?

Settings of the Python interpreter itself.

The `sys` module provides an access point to the Python environment. You find there command line arguments, the import path settings, the standard input, output and error stream and many more.

### Installed with Python by default

yes

### Example

Command line parameters used when calling Python:

    import sys
    print(sys.argv)

Version of the Python interpreter:

    print(sys.version)

Directories in which Python looks for modules:

    print(sys.path)


Exit Python altogether:

    sys.exit()
    
### Where to learn more?

[https://docs.python.org/3/library/sys.html](https://docs.python.org/3/library/sys.html)
