#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

grammar = Grammar(u'Grammaire terminal')

class ChepTerminal(MappingRule):
	mapping = {
		u'liste fichiers': Text(u'ls') + Key(u'enter'),
		u'liste complète': Text(u'ls -lh') + Key(u'enter'),
		u'terminal suivant': Key(u's-right'),
		u'terminal précédent': Key(u's-left'),
		u'nouveau terminal': Key(u'cs-t'),
	}
	extras = [
		Dictation(u'text'),
		Integer('n', 0, 10000000),
	]
	defaults = {
		'n': 1,
	}


grammar.add_rule(ChepTerminal())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
