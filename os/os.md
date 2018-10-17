
# os

### What it is good for?

Working with files and directories.

The `os` module provides an easy way to interact with files, directories and other parts of your operating system. It contains many functions to list, change, copy, remove and examine files and directories.

### Installed with Python by default

yes

### Example

Change directory and list its contents:

    import os

    os.chdir('/home/krother/python_modules/')
    os.listdir('.')

    ['sys.md', 'os.md', 'csv.md', 're.md', 'random.md', 
    'pprint.md', 'numpy.md', 'time.md', 'itertools.md', 
    'json.md', 'template.md', 'math.md', 'urllib.md']

Check whether a file exists:

    os.path.exists('os.md')

Copy a file and remove it afterwards:

    os.system('cp os.md copy.md')
    os.remove('copy.md')

### Where to learn more?

[https://docs.python.org/3/library/os.html](https://docs.python.org/3/library/os.html)
