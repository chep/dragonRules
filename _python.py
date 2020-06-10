#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

def creeBlock(type='mauvais type'):
	_type = unicode(type)
	action = Text(u'')

	switcher = {
		u'if': u'if',
		u'if sinon': u'ife',
		u'tant que': u'while',
		u'temps que': u'wh', #au cas où on serait mal compris
		u'avec': u'with',
		u'pour': u'for',
		u'fonction': u'f',
		u'init': u'init',
		u'imite': u'init', #au cas où on serait mal compris
	}
	action = Text(switcher.get(_type, ''))
	action += Key(u'tab')
	action.execute()

class ChepBlocks(MappingRule):
	mapping = {
		u'block <type>': Function(creeBlock),
	}
	extras = [
		Dictation(u'type'),
	]

class ChepImport(MappingRule):
	mapping = {
		u'import from': Text(u'from') + Key(u'tab'),
		}

class ChepTags(MappingRule):
	mapping = {
		u'cherche tag': Key(u'c-c,dot'),
	}

def grammairePython():
	grammarPy = Grammar('Grammaire python')
	grammarPy.add_rule(ChepImport())
	grammarPy.add_rule(ChepBlocks())
	grammarPy.add_rule(ChepTags())
	return grammarPy

