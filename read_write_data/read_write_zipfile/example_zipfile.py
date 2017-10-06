
# Create a new zip archive and add files to it:

import zipfile
z = zipfile.ZipFile('archive.zip', 'w')
z.write('myfile.txt')                   # has to exist
z.writestr('test.txt', 'Hello World')   # new
z.close()


# List contents of the newly created zip file:

z = zipfile.ZipFile('archive.zip')
print(z.namelist())


# Extract a file to a new folder:

print(z.extract('test.txt', 'myfolder'))
z.close()
