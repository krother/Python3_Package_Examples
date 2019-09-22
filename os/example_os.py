
import os

# Change directory and list its contents:
os.chdir('/home/krother/python_modules/')
os.listdir('.')

# Check whether a file exists:
os.path.exists('README.md')

# Copy a file
os.system('cp README.md copy.md')

# Remove a file
os.remove('copy.md')
