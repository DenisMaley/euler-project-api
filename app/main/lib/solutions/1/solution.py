def sum_ap(n: int, d: int) -> int:
    # amount of terms in the arithmetic progression
    n = int(n / d)

    return int(n * (n + 1) * d / 2)


def sum_multiples_two_dividers(n: int, d1: int, d2: int) -> int:
    return int(sum_ap(n - 1, d1) +
               sum_ap(n - 1, d2) -
               sum_ap(n - 1, d1 * d2))
