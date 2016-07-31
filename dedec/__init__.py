# -*- coding: utf-8 -*-
#
__all__ = [
    'dedec', 'repr'
    ]

__version__ = '0.2.1'
__author__ = 'Nico Schlömer'
__author_email__ = 'nico.schloemer@gmail.com'
__website__ = 'https://github.com/nschloe/dedec'


def dedec(a, max_denominator=100, abs_tol=1.0e-15):
    from math import pi, exp, log, sin, cos, tan, asin, acos, atan
    from fractions import gcd

    # We need a list of tuples here since we rely on the ordering. A dict
    # doesn't have that.
    funs = [
            (None, lambda x: x, lambda x: x),
            ('sqrt', lambda x: x**0.5, lambda x: x**2),
            ('root3', lambda x: x**(1.0/3.0), lambda x: x**3)
            ]

    if a > 0:
        funs.append(('exp', exp, log))

    funs.append(('logn', log, exp))

    if a >= -1.0 and a <= 1.0:
        funs.append(('sin', sin, asin))
        funs.append(('cos', cos, acos))

    funs.append(('tan', tan, atan))

    sols = []
    for fun_name, fun, inv in funs:
        a0 = a
        a0 = inv(a0)
        for mult_pi in range(3):
            a1 = a0 / pi**mult_pi

            for den in range(1, max_denominator+1):
                num = int(round(a1*den))
                if gcd(num, den) > 1:
                    continue
                diff = a1 - float(num) / den
                if abs(diff) < abs_tol:
                    error = a - fun(float(num) / den * pi**mult_pi)
                    sols.append((num, den, mult_pi, fun_name, error))

    return sols


def repr(num, denom, mult_pi, fun_name):

    num_str = '%d' % num

    if denom > 1:
        num_str += ' / %d' % denom

    if mult_pi == 1:
        num_str += ' * pi'
    elif mult_pi > 1:
        num_str += ' * pi^%d' % mult_pi

    if fun_name is None:
        return '%s' % num_str

    return '%s(%s)' % (fun_name, num_str)