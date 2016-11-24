
# zipfile

### What it is good for?

Read and write `.zip` files.

You can add both existing files and strings to a zip file. If you are adding strings you need to specify the file name it is written to. When you extract files to a folder, the output folder is automatically created.

### Installed with Python by default

yes

### Example

Create a new zip archive and add files to it:

    >>> import zipfile
    >>> z = zipfile.ZipFile('archive.zip', 'w')
    >>> z.write('myfile.txt')                   # has to exist
    >>> z.writestr('test.txt', 'Hello World')   # new
    >>> z.close()

List contents of the newly created zip file:

    >>> z = zipfile.ZipFile('archive.zip')
    >>> z.namelist()
    ['test.txt', 'myfile.txt']

Extract a file to a new folder:

    >>> z.extract('test.txt', 'myfolder')
    'myfolder/test.txt'
    >>> z.close()

### Where to learn more?

[docs.python.org/3/library/zipfile.html](https://docs.python.org/3/library/zipfile.html)

