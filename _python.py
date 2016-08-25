#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire python')

class ChepPython(MappingRule):
	mapping = {
		'python tag': Key(u'a-dot'),
		'python reviens': Key(u'a-colon') + Text(u'(pop-tag-mark)') + Key(u'enter'),
	}
	extras = [
		Dictation(u'text'),
		Integer('n', 0, 10000000),
	]
	defaults = {
		'n': 1,
	}

grammar.add_rule(ChepPython())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
