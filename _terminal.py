#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

grammar = Grammar(u'Grammaire terminal')

class ChepTerminal(MappingRule):
	mapping = {
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

class ChepCommandes(MappingRule):
	mapping = {
		u'liste fichiers': Text(u'ls') + Key(u'enter'),
		u'liste complète': Text(u'ls -lh') + Key(u'enter'),
		u'monte usb <lettre> [<n>]': Text(u'mount /dev/sd'
		                                  + u'%(lettre)s'.lower()
		                                  + u'%(n)d') + Key(u'enter'),
		u'démonte usb': Text(u'umount /media/usb') + Key(u'enter'),
		u'tar décompresse': Text(u'tar xf '),
		u'tar compresse': Text(u'tar czf '),
		u'cd': Text(u'cd '),
		u'ssh': Text(u'ssh '),
	}
	extras = [
		Choice(u'lettre', { u'alpha': u'a',
		                    u'bravo': u'b',
		                    u'charlie': u'c',
		                    u'delta': u'd',
		                  }
		),
		Integer('n', 0, 10000000),
	]
	defaults = {
		'n': 1,
	}

class ChepApplication(MappingRule):
	mapping = {
		u'lance vinagre': Text(u'vinagre >/dev/null 2>&1 &') + Key(u'enter'),
	}

grammar.add_rule(ChepTerminal())
grammar.add_rule(ChepCommandes())
grammar.add_rule(ChepApplication())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
