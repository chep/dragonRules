#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *

grammar = Grammar('Grammaire magit')

class ChepMagit(MappingRule):
	mapping = {
		u'git status': Key(u'c-c,m,s'),
		u'commit': Key(u'c-c,c-c'),
		u'svn commit': Key(u'a-x') + Text(u'magit-svn-dcommit') + Key('enter'),
		u'svn rebase': Key(u'a-x') + Text(u'magit-svn-rebase') + Key('enter'),
		u'svn fetch': Key(u'a-x') + Text(u'magit-svn-fetch') + Key('enter'),
		u'git blame': Key(u'a-x') + Text(u'magit-blame') + Key('enter'),
	}


grammar.add_rule(ChepMagit())
grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
