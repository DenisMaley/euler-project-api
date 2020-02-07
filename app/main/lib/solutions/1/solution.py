def sumAP(n, d):
    # amount of terms in the arithmetic progression
    n = int(n / d)

    return n * (n + 1) * d / 2


def sumMultiplesTwoDividers(n, d1, d2):
    return int(sumAP(n - 1, d1) +
               sumAP(n - 1, d2) -
               sumAP(n - 1, d1 * d2))
