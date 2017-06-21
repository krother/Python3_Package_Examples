
# Change directory and list its contents:

import os

os.chdir('/home/krother/python_modules/')
os.listdir('.')


# Check whether a file exists:

os.path.exists('os.md')


# Copy a file and remove it afterwards:

os.system('cp os.md copy.md')
os.remove('copy.md')
