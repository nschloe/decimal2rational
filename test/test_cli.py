# -*- coding: utf-8 -*-
#
import dedec


def test_cli():
    dedec.cli.main(["{:f}".format(3.0 / 7.0)])
    return