import twokenize

def tokens(string, lower=True):
    if lower:
        return twokenize.tokenize(string.lower())
    else:
        return twokenize.tokenize(string)
