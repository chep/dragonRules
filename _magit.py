#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
