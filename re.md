
# re

### What it is good for?

Pattern matching in text.

The `re` module implements **Regular Expression**, a powerful syntax for searching patterns in text. Regular Expressions are available in most programming languages. You need to learn some special characters to build your own patterns.

### Installed with Python by default

yes

### Example

    >>> import re

    >>> text = "the quick brown fox jumps over the lazy dog"

Search for `o` and show adjacent characters:

    >>> re.findall(".o.", text)
    ['row', 'fox', ' ov', 'dog']

Search for three-letter words enclosed by whitespace:

    >>> re.findall("\s(\wo\w)\s*", text)
    ['fox', 'dog']

Substitute any of `dflj` by a `w`:

    >>> re.sub("[dflj]", "w", text)
    'the quick brown wox wumps over the wazy wog'

Check if `jumps` or `swims` occurs and return details:

    >>> re.search('jumps|swims', text)
    <_sre.SRE_Match object; span=(20, 25), match='jumps'>

### Where to learn more?

[http://regexone.com/](http://regexone.com/)

[https://docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
