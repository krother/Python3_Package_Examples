
# os

### What it is good for?

Working with files and directories.

The `os` module provides an easy way to interact with files, directories and other parts of your operating system. It contains many functions to list, change, copy, remove and examine files and directories.

### Installed with Python by default

yes

### Example

Change directory and list its contents:

    >>> import os

    >>> os.chdir('/home/krother/Desktop/courses/python/')
    >>> os.listdir('module_handout')
    ['sys.md', 'os.md', 'csv.md', 're.md', 'random.md', 
    'pprint.md', 'numpy.md', 'time.md', 'itertools.md', 
    'json.md', 'template.md', 'math.md', 'urllib.md']

Check whether a file exists:

    >>> os.path.exists('module_handout/template.md')

Copy a file and remove it afterwards:

    >>> os.system('cp module_handout/template.md test.md')
    >>> os.remove('test.md')

### Where to learn more?

[https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)
