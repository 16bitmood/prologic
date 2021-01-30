from prologic.tokens import Var
from prologic.lexer import lex
from prologic.my_parser import parse
from prologic.evaluator import evaluate
from prologic.truth_table import truth_table

STARTUP_MSG = '''
=========================
* Prologic :

- A Propositional Logic Statement Evaluator.
- Options:
(d) enable debug mode
(e) for examples
(h) to display this msg
(i) to evaluate at a given input
(q) to quit
'''

EXAMPLE_MSG = '''
=========================
# Basic Example:

>> !p
---------------------
         p|        ¬p
---------------------
         1|         0
         0|         1
---------------------

# Input Example:

>> i
Expr >> p->q
Vars >> p = 0, q = 1
Result :

=========================
'''


# Helper Function
def evaluate_from_src(src, args, dbg):
    if dbg:
        print('args: ', args)
        print('lex: ', lex(src))
        print('parse: ', parse(lex(src)))
    return evaluate(parse(lex(src)), args)


# REPL
def main():
    DEBUG = False
    print(STARTUP_MSG)
    while True:
        c = input('>> ')

        if c == 'h':
            print(STARTUP_MSG)

        elif c == 'e':
            print(EXAMPLE_MSG)

        elif c == 'q':
            quit()

        elif c == 'd':
            print('Debug Mode Enabled!')
            DEBUG = True

        elif c == 'i':
            src = input('Expr >> ')
            val = input('Vars >> ')
            vars_dict = [v.split('=') for v in val.split(',')]
            vars_dict = {Var(name.strip()):
                         True if val.strip() == '1' else False
                         for name, val in vars_dict}

            print('Result: ', int(evaluate_from_src(src, vars_dict, DEBUG)))

        else:
            truth_table(c, dbg=DEBUG)
