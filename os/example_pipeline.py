
# example phrases useful for building pipelines:

# do something for all files in a directory
import os

for filename in os.listdir("/home/participant/"):
    if filename.endswith(".py"):
        print filename


# run a command-line program
os.system("ls -l > result.txt")


# give parameters to a Python program
import sys
print sys.argv
"""
Try calling this program with:

python example_pipeline.py
python example_pipeline.py input.seq
python example_pipeline.py 1 2 3

You should see a difference.
"""
