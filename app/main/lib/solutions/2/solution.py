even_fib = [0, 2]


def next_even_fib() -> int:
    return 4 * even_fib[-1] + even_fib[-2]


# TODO After migrating to Python 3.8 simplify the loop
# using assignment expressions
# https://www.python.org/dev/peps/pep-0572/#sysconfig-py
# https://stackoverflow.com/questions/50297704/syntax-and-assignment-expressions-what-and-why
def sum_even_fib(limit: int) -> int:
    while next_even_fib() < limit:
        even_fib.append(next_even_fib())
    return sum(even_fib)
