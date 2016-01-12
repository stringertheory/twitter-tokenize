This evolved from [this project](https://github.com/brendano/tweetmotif), but only retained the tokenization stuff.

Install with:
```bash
pip install git+https://github.com/stringertheory/twitter-tokenize.git#egg=twitter-tokenize
```

and run with:
```python
import twokenize

twokenize.tokens("Here's the thing: yo mama ;)")
# [u'here', u"'s", u'the', u'thing', u':', u'yo', u'mama', u';)']
```
