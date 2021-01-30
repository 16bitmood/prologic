import itertools
from copy import deepcopy as cp

from tokens import Var, ABSOLUTES
from lexer import lex
from my_parser import parse
from evaluator import evaluate

# Global Constants
op_to_str = {
    'implication': '⇒',
    'equivalence': '⇔',
    'conjunction': '∧',
    'disjunction': '∨',
    'negation': '¬',
    'xor': '⊕'
}


# Helper Functions
def get_sub_exprs(expr, last_call=True):
    if isinstance(expr, Var):
        return set()

    sub_exprs = {expr}
    for a in expr[1:]:
        sub_exprs |= get_sub_exprs(a, False)

    if last_call:
        return sorted(list(sub_exprs), key=lambda x: len(expr_to_str(x)))
    else:
        return sub_exprs


def get_variables(expr, last_call=True):
    if isinstance(expr, Var):
        return {expr}

    vs = set()
    for x in expr[1:]:
        vs |= get_variables(x, False)

    if last_call:
        return list(vs)
    else:
        return vs


def get_all_inputs(variables):
    return itertools.product([True, False], repeat=len(variables))


def expr_to_str(expr):
    if isinstance(expr, Var):
        return expr.s

    # Infix Binary Operators
    if expr[0] in ['implication', 'equivalence',
                   'conjunction', 'disjunction', 'xor']:
        left = expr_to_str(expr[1])
        operator = op_to_str[expr[0]]
        right = expr_to_str(expr[2])

        return f'({left}{operator}{right})'

    # Prefix Unary Operators
    elif expr[0] in ['negation']:
        operator = op_to_str[expr[0]]
        right = expr_to_str(expr[1])

        return f'({operator}{right})'


# Gen Truth Table of an expr
def gen_truth_table(expr):
    variables = get_variables(expr)
    sub_exprs = get_sub_exprs(expr)

    header = variables + sub_exprs

    all_inputs = get_all_inputs(variables)

    rows = []
    for val in all_inputs:
        vars_dict = {k: v for k, v in zip(variables, val)} | ABSOLUTES
        results = [evaluate(cp(se), vars_dict) for se in sub_exprs]

        variable_values = []
        for i, v in enumerate(variables):
            if v in ABSOLUTES.keys():
                variable_values.append(ABSOLUTES[v])
            else:
                variable_values.append(vars_dict[v])

        rows.append(variable_values + results)

    return header, rows


# Pretty Print a Truth Table
def pprint_truth_table(header, rows):
    header = [hs if isinstance(h, Var) else hs[1:-1]
              for h, hs in zip(header, map(expr_to_str, header))]

    fmt = '|'.join(['{:>10}']*len(header))
    header = fmt.format(*header)

    print('-'*len(header))
    print(header)
    print('-'*len(header))

    for r in rows:
        print(fmt.format(*r))
    print('-'*len(header))


# Main Function
def truth_table(src):
    tokens = lex(src)
    expr = parse(tokens)
    header, rows = gen_truth_table(expr)
    pprint_truth_table(header, rows)
    return header, rows
