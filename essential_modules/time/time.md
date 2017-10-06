
# time

### What it is good for?

Simple handling of times and dates.

The functions in `time` return the time and date in a structured format that can be formated to custom strings.

### Installed with Python by default

yes

### Example

The `time` module offers functions for getting the current time and date.

    import time

    print(time.asctime())

    print(time.strftime('%a %d.%m.', time.localtime()))

Wait for two seconds:

    time.sleep(2)


The `datetime` module also helps to format dates:

    date = datetime.date(2015, 12, 24)
    date.strftime("%d.%m.%Y")
        
Dates can be converted to integer numbers:

    date = datetime.date(2015, 12, 24)
    number = date.toordinal()

and back

    datetime.date.fromordinal(7)

### Where to learn more?

* [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/time.html)
* [https://docs.python.org/3/library/time.html](https://docs.python.org/3/library/datetime.html)
