
# re

### What it is good for?

Pattern matching in text.

The `re` module implements **Regular Expression**, a powerful syntax for searching patterns in text. Regular Expressions are available in most programming languages. You need to learn some special characters to build your own patterns.

### Installed with Python by default

yes

### Example

    import re

    text = "the quick brown fox jumps over the lazy dog"

Search for `o` and show adjacent characters:

    re.findall(".o.", text)
    print(re.findall(".o.", text))

    ['row', 'fox', ' ov', 'dog']

Search for three-letter words enclosed by whitespace:

    print(re.findall("\s(\wo\w)\s*", text))
        
    ['fox', 'dog']

Substitute any of `dflj` by a `w`:

    print(re.sub("[dflj]", "w", text))
    
    'the quick brown wox wumps over the wazy wog'

Check if `jumps` or `swims` occurs and return details:

    print(re.search('jumps|swims', text))
    
    <_sre.SRE_Match object; span=(20, 25), match='jumps'>

### Where to learn more?

#### Online Games

* [regexone.com/](http://regexone.com/) - Learn regular expressions by simple, interactive examples. Great place to start.
* [Regex crossword](http://regexcrossword.com/) - Train proper use of single characters, wildcards and square brackets. Easy.
* [Regex Practice Quiz 1](http://www.tekdefense.com/news/2013/2/10/regex-practice-quiz-1-understanding-patterns.html) - exercises to try offline.
* [Regex golf](http://regex.alf.nu) - Advanced exercises. Match as many phrases with as few key strokes as possible.

#### Reference

* [Python Regex HOWTO](https://docs.python.org/3.6/howto/regex.html)
* [docs.python.org/3/library/re.html](https://docs.python.org/3/library/re.html)
* [Quick Reference](http://www.night-ray.com/regex.pdf) - a reference sheet for looking up metacharacters. Uses the **Python syntax**.

## Online Regex Testers

* [Regex 101](http://regex101.com/) - Shows matched text with explanation.
* [Pythex](https://pythex.org/) - RegEx tester using the Python `re` module.
* [regexpal](http://regexpal.com/) - Uses JavaScript to highlight matches.
