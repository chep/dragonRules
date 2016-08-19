#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer

grammar = Grammar('Grammaire ELTA')

class ChepConnexions(MappingRule):
	mapping = {
		'connexion <n>': Text('ssh -Y user@172.16.131.%(n)d') + Key('enter'),
	}

	extras = [
		IntegerRef('n', 0, 1000),
	]
	defaults = {
		'n': 0,
	}

grammar.add_rule(ChepConnexions())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
