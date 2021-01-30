# Allowed symbols
SYMBOLS = '⇒⇔¬∧∨⊕()'  # TODO?: '∀∃⊢'


class Var:
    '''
    Variable token: A way to differentiate variables from symbols
    '''

    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return self.s

    def __str__(self):
        return self.s

    def __eq__(self, other):
        if type(self) == type(other):
            return self.s == other.s

    def __hash__(self):
        return self.s.__hash__()


# Absolute values
ABSOLUTES = {Var('⊤'): True, Var('⊥'): False}
