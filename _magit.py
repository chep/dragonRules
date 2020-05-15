#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire magit')

class ChepMagit(MappingRule):
	mapping = {
		u'guit status': Key(u'c-c,m,s'),
		u'guit commit': Key(u'c,c'),
		u'guit amende': Key(u'c,a'),
		u'guit fetch': Key(u'f,u'),
		u'guit poule': Key(u'F,u'),
		u'svn commit': Key(u'a-x') + Text(u'magit-svn-dcommit') + Key('enter'),
		u'svn rebase': Key(u'a-x') + Text(u'magit-svn-rebase') + Key('enter'),
		u'svn fetch': Key(u'a-x') + Text(u'magit-svn-fetch') + Key('enter'),
		u'guit blame': Key(u'a-x') + Text(u'magit-blame') + Key('enter'),
	}


grammar.add_rule(ChepMagit())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
