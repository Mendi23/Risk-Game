from itertools import product
from math import gcd

def score_pair(x1: int, x2: int) -> int: # 1 or -1  
    return 1 if x1 > x2 else -1

def score(a_dice, d_dice) -> int: #  -2 >= return < 2
    return sum(score_pair(*p) for p in zip(sorted(a_dice, reverse=True), sorted(d_dice, reverse=True)))

def simplify_fraction(a, b) -> tuple(int, int):
    x = gcd(a,b)
    return a//x, b//x

def calculate_pct(a: int, d: int) -> None:
    a_throw = product(range(1,7), repeat=a)
    d_throw = product(range(1,7), repeat=d)
    r = sum((score(a, d) for a, d in product(a_throw, d_throw)))
    print(simplify_fraction(r, (6**(a+d))))

if __name__ == "__main__":
    calculate_pct(2, 1)
    pass



