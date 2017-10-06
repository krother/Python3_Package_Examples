
# Installing matplotlib for Python3

## 1. create virtualenv for python3

export VIRTUALENV_PYTHON=/usr/bin/python3
mkvirtualenv plots
setvirtualenvproject ~/.virtualenvs/plots .


## 2. install pip3

sudo apt-get python-pip3


## 3. upgrade setuptools

pip3 install --upgrade setuptools


# 4. install dev package for libfreetype

sudo apt-get install libfreetype6
sudo apt-get install libfreetype6-dev


## 5. install matplotlib

pip3 install matplotlib


# DETAILED STEPS IF STEP 4 FAILS

## 6. get matplotlib source from github

git clone https://github.com/matplotlib/matplotlib.git


## 7. install dependencies via pip3

pip3 -r requirements.txt

# requirements.txt:
# freetype-py==1.0.1
# matplotlib==1.5.dev1
# nose==1.3.6
# numpy==1.9.2
# pyparsing==2.0.3
# python-dateutil==2.4.2
# pytz==2015.2
# six==1.9.0


## 8. install matplotlib

python setup.py build
python setup.py install


## 9. test

python

>>> import pylab as plt
>>> plt.plot(range(10))
>>> plt.savefig('plot.png')
