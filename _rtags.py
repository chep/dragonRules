#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire rtags')

class ChepRtags(MappingRule):
	mapping = {
		'cherche tag': Key(u'a-semicolon'),
		'retour tag': Key(u'a-asterisk'),
		'info tag': Key(u'alt:down,c-semicolon,alt:up'),
	}


grammar.add_rule(ChepRtags())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
