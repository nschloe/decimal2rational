# -*- coding: utf-8 -*-
#
__all__ = [
    'decimal2rational'
    ]

__version__ = '0.2.0'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/decimal2rational'


def decimal2rational(a, max_denominator=1000, tol=1.0e-15):
    from math import pi, exp, log

    funs = [
        (lambda x: x, None),
        (lambda x: x**2, 'sqrt'),
        (lambda x: x**3, 'root3')
        ]

    if a > 0:
        funs.append((lambda x: log(x), 'exp'))

    funs.append((lambda x: exp(x), 'logn'))

    for fun, fun_name in funs:
        a0 = a
        a0 = fun(a0)
        for mult_pi in range(2):
            if mult_pi > 0:
                a0 /= pi**mult_pi

            for den in range(1, max_denominator+1):
                rd = round(a0*den)
                diff = a0*den - rd
                if abs(diff) < tol * a0*den:
                    return int(rd), den, mult_pi, fun_name, diff

    return None, None, None, None, None
