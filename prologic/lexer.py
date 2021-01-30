from tokens import Var, SYMBOLS


# Helper Functions
def convert_to_unicode(src):
    '''
    Converts input into a uniform unicode string representation
    '''
    # Order here matters!
    rs = [('and', '∧'), ('&', '∧'),
          ('or', '∨'), ('|', '∨'),
          ('not', '¬'), ('!', '¬'),
          ('<->', '⇔'), ('->', '⇒'),
          ('=', '⇔'),
          ('^', '⊕')]
    for f, t in rs:
        src = src.replace(f, t)

    return src


def pad_symbols(src):
    '''
    Adds space before and after unicode symbols
    '''
    for s in SYMBOLS:
        src = src.replace(s, f' {s} ')
    return src


# Main Function
def lex(src):
    '''
    Converts a string into a list of tokens.
    '''
    src = convert_to_unicode(src)
    src = pad_symbols(src)
    return [Var(x) if x not in SYMBOLS else x for x in src.split()]
