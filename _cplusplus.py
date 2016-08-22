#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer

grammar = Grammar('Grammaire C++')




def creeBlock(type='mauvais type'):
	_type = str(type)
	action = Text('')

	switcher = {
		'if': 'if',
		'sinon': 'else',
		'tant que': 'while',
		'pour': 'for',
		'switch': 'switch',
		'classe': 'cls',
	}

	action = Text(switcher.get(_type, ''))
	action += Key('tab')
	action.execute()

def creeInstruction(type='mauvais type'):
	_type = str(type)
	action = Text(u'')
	if _type == 'retour':
		action = Text('return ;')
		action += Key('left')
	action.execute()

def concatene(p_words):
	chaine = str(p_words[0])
	for w in p_words[1:]:
		chaine += str(w).title()
	return chaine

def membre(nom):
	action = Text('m_')
	if isinstance(nom, NatlinkDictationContainer):
		action += Text(concatene(nom.words))
	action.execute()

def parametre(nom):
	action = Text('p_')
	if isinstance(nom, NatlinkDictationContainer):
		action += Text(concatene(nom.words))
	action.execute()


class ChepBlocks(MappingRule):
	mapping = {
		'block <type>': Function(creeBlock),
		'instruction <type>': Function(creeInstruction),
		'membre [<nom>]': Function(membre),
		'parametre [<nom>]': Function(parametre),
	}
	extras = [
		Dictation(u'type'),
		Dictation(u'nom'),
	]
	defaults = {
		'nom': '',
	}

class ChepClasses(MappingRule):
	mapping = {
		'constructeur': Text('ct') + Key('tab'),
		'fonction': Text('f') + Key('tab') + Text('function') + Key('enter'),
		'declaration': Text('f') + Key('tab') + Text('fun_declaration') + Key('enter'),
		'prive': Text('private:') + Key('tab') + Key('enter'),
	}

grammar.add_rule(ChepBlocks())
grammar.add_rule(ChepClasses())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
