#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer

def concatene(p_words):
	chaine = unicode(p_words[0]).lower()
	for w in p_words[1:]:
		chaine += unicode(w).title()
	return chaine

def membre(nom):
	action = Text(u'm_')
	if isinstance(nom, NatlinkDictationContainer):
		action += Text(concatene(nom.words))
	action.execute()

def parametre(nom):
	action = Text(u'p_')
	if isinstance(nom, NatlinkDictationContainer):
		action += Text(concatene(nom.words))
	action.execute()

def variable(nom):
	if isinstance(nom, NatlinkDictationContainer):
		action = Text(concatene(nom.words))
	action.execute()

class ChepVariable(MappingRule):
	mapping = {
		u'membre [<nom>]': Function(membre),
		u'parametre [<nom>]': Function(parametre),
		u'variable [<nom>]': Function(variable),
	}
	extras = [
		Dictation(u'nom'),
	]
	defaults = {
		u'nom': u'',
	}
