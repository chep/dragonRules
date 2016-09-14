#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire rtags')

class ChepRtags(MappingRule):
	mapping = {
		u'cherche tag': Key(u'a-semicolon'),
		u'retour tag': Key(u'a-asterisk'),
		u'info tag': Key(u'ca-semicolon'),
		u'occurrence': Key(u'c-c,r,slash'),
		u'complétion': Key(u'c-tab'),
	}


grammar.add_rule(ChepRtags())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
