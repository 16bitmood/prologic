from truth_table import truth_table


def repl():
    msg = 'Enter Expression(q to quit):'
    while True:
        c = input(msg)
        if c == 'q':
            quit()
        else:
            truth_table(c)


if __name__ == '__main__':
    repl()
