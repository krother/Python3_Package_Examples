
# find all files that match a certain pattern in a directory tree.

import os, fnmatch

pattern = '*.py'

for path, subdirs, files in os.walk('.'):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                print(os.path.join(path, name))
