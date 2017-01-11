#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer

grammar = Grammar('Grammaire ELTA')

class ChepConnexions(MappingRule):
	mapping = {
		u'connexion <n> point <p> [<text>]': Text(u'ssh -Y %(text)s@172.16.%(n)d.%(p)d') + Key(u'enter'),
		u'telnet châssis': Text(u'telnet localhost 5025') + Key(u'enter'),
		u'connexion carte <n>': Text(u'ssh root@203.0.113.%(n)d') + Key(u'enter'),
	}

	extras = [
		IntegerRef('n', 0, 1000),
		IntegerRef('p', 0, 1000),
		Dictation("text"),
	]
	defaults = {
		'n': 0,
		'p': 0,
		'text': u'user',
	}

grammar.add_rule(ChepConnexions())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
