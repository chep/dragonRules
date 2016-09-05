#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire magit')

class ChepMagit(MappingRule):
	mapping = {
		u'maguit': Key(u'c-c,m,s'),
		u'commit': Key(u'c-c,c-c'),
		u'commit svn': Key(u'a-x') + Text(u'magit-svn-dcommit') + Key('enter'),
	}


grammar.add_rule(ChepMagit())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
