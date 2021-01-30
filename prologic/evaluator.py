from prologic.tokens import Var

op = {
    'implication': lambda x, y: y if x else True,  # a -> b
    'equivalence': lambda x, y: x == y,  # a = b
    'conjunction': lambda x, y: x and y,  #
    'disjunction': lambda x, y: x or y,  # or
    'negation': lambda x: not x,  # not
    'xor': lambda x, y: x ^ y
}


# Helper Functions
def set_var(expr, var, var_value):
    if expr == var:
        return var_value
    elif isinstance(expr, Var):
        return expr
    elif isinstance(expr, bool):  # Already Set
        return expr
    return [expr[0]] + [set_var(x, var, var_value) for x in expr[1:]]


def set_vars(expr, args):
    for var, value in args.items():
        expr = set_var(expr, var, value)
    return expr


def eval_expr(expr):
    if not isinstance(expr, list):
        return expr
    return op[expr[0]](*[eval_expr(x) for x in expr[1:]])


# Main Function
def evaluate(expr, args):
    '''
    Evaluates a logic statement with given args

    Args:
        expr: Parsed Expression
        args: a dict with var_name, value pairs
    '''
    expr = set_vars(expr, args)
    return eval_expr(expr)
