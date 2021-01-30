from prologic.lexer import Var


class Parser:
    def __init__(self, tokens):
        self.ts = tokens
        self.i = 0  # Index

    # Mutator Functions
    def advance(self):
        if self.i+1 != len(self.ts):
            self.i += 1
            return self.ts[self.i-1]

        return self.ts[self.i]

    def peek(self):
        if self.i+1 != len(self.ts):
            return self.ts[self.i+1]

        return self.ts[self.i]

    def current(self):
        return self.ts[self.i]

    def consume(self, seq):
        for s in seq:
            assert s == self.advance()

    # Recursive Descent Parser
    def parse(self):
        return self._equivalence()

    def _equivalence(self):
        left = self._implication()
        while self.current() == '⇔':
            self.advance()
            right = self._implication()
            left = ('equivalence', left, right)
        return left

    def _implication(self):  # ->
        left = self._conjunction()
        while self.current() == '⇒':
            self.advance()
            right = self._conjunction()
            left = ('implication', left, right)
        return left

    def _conjunction(self):  # and
        left = self._disjunction()
        while self.current() == '∧':
            self.advance()
            right = self._disjunction()
            left = ('conjunction', left, right)
        return left

    def _disjunction(self):  # or
        left = self._xor()
        while self.current() == '∨':
            self.advance()
            right = self._xor()
            left = ('disjunction', left, right)
        return left

    def _xor(self):
        left = self._negation()
        while self.current() == '⊕':
            self.advance()
            right = self._negation()
            left = ('xor', left, right)
        return left

    def _negation(self):  # not
        if self.current() == '¬':
            self.advance()
            expr = self._primary()
            return ('negation', expr)
        else:
            return self._primary()

    def _primary(self):
        c = self.advance()
        if isinstance(c, Var):
            return c
        elif c == '(':
            expr = self.parse()
            self.consume(')')
            return expr


def parse(tokens):
    '''
    Converts a list of tokens into an abstract syntax tree
    '''
    parser = Parser(tokens)
    return parser.parse()
