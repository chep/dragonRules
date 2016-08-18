#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>

from aenea import *

grammar = Grammar('Grammaire magit')

class ChepMagit(MappingRule):
    mapping = {
        'maguit': Key(u'c-c,m,s'),
        'commit': Key(u'c-c,c-c'),
    }


grammar.add_rule(ChepMagit())
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
