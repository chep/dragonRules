#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer
from subprocess import call

grammar = Grammar('Grammaire Sway')

def bureauN(n):
	switcher = {
		1 : u'&',
		2 : u'é',
		3 : u'"',
		4 : u'\'',
		5 : u'(',
		6 : u'-',
		7 : u'è',
		8 : u'_',
		9 : u'ç',
		0 : u'à',
	}
	action = Key(u'win:down') + Text(switcher.get(n)) + Key(u'win:up')
	action.execute()


class ChepSway(MappingRule):
	mapping = {
		u'Souhait envoie bureau <n>': Key(u'w-%(n)d'),
		u'Souhait bureau <n>': Function(bureauN),
		u'Souhait gauche': Key(u'w-left'),
		u'Souhait droite': Key(u'w-right'),
		u'Souhait haut': Key(u'w-up'),
		u'Souhait bas': Key(u'w-down'),
		u'Souhait déplace gauche': Key(u'shift:down') + Key(u'w-left') + Key(u'shift:up'),
		u'Souhait déplace droite': Key(u'shift:down') + Key(u'w-right') + Key(u'shift:up'),
		u'Souhait déplace haut': Key(u'shift:down') + Key(u'w-up') + Key(u'shift:up'),
		u'Souhait déplace bas': Key(u'shift:down') + Key(u'w-down') + Key(u'shift:up'),
		u'Souhait ferme fenêtre': Key(u'shift:down') + Key(u'w-q') + Key(u'shift:up'),
		u'Souhait terminal': Key(u'w-enter'),
	}
	extras = [
		IntegerRef('n', 0, 1000),
	]
	defaults = {
		'n': 1,
	}


grammar.add_rule(ChepSway())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
