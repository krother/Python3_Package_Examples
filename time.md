
# time

### What it is good for?

Simple handling of times and dates.

The functions in `time` return the time and date in a structured format that can be formated to custom strings.

### Installed with Python by default

yes

### Example

Format the current time to a string:

    >>> import time
    >>> time.asctime()
    'Fri Mar 18 19:15:24 2016'
    >>> time.strftime('%a %d.%m.', time.localtime())
    'Fri 18.03.'

Waiting for two seconds:

    >>> time.sleep(2)

### Where to learn more?

[https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)
