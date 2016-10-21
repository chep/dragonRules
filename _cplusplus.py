#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer


def creeBlock(type='mauvais type'):
	_type = unicode(type)
	action = Text(u'')

	switcher = {
		u'if': u'if',
		u'sinon': u'else',
		u'tant que': u'while',
		u'temps que': u'while',
		u'pour': u'for',
		u'switch': u'switch',
		u'classe': u'cls',
		u'exception': u'try',
		u'énumération': u'enum',
		u'structure': u'struct',
	}
	action = Text(switcher.get(_type, ''))
	action += Key(u'tab')
	action.execute()

def creeInstruction(type=u'mauvais type'):
	_type = unicode(type)
	action = Text(u'')
	switcher = {
		u'retour': Text(u'return ;') +  Key(u'left'),
	}
	action = switcher.get(_type, 'defaut')
	action.execute()

def concatene(p_words):
	chaine = str(p_words[0])
	for w in p_words[1:]:
		chaine += str(w).title()
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


class ChepBlocks(MappingRule):
	mapping = {
		u'block <type>': Function(creeBlock),
		u'instruction <type>': Function(creeInstruction),
	}
	extras = [
		Dictation(u'type'),
	]

class ChepClasses(MappingRule):
	mapping = {
		u'constructeur': Text(u'ct') + Key(u'tab'),
		u'fonction': Text(u'f') + Key(u'tab') + Text(u'function') + Key(u'enter'),
		u'fonction main': Text(u'main') + Key(u'tab'),
		u'declaration': Text(u'f') + Key(u'tab') + Text(u'fun_declaration') + Key(u'enter'),
		u'privé': Text(u'private:') + Key(u'tab') + Key(u'enter'),
		u'public': Text(u'public:') + Key(u'tab') + Key(u'enter'),
		u'protégé': Text(u'protected:') + Key(u'tab') + Key(u'enter'),
	}


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


class ChepType(CompoundRule):
	spec = u'type <nom>'
	extras = [Choice(u'nom', { u'entier': u'int',
	                           u'bool': u'bool',
	                           u'non signé': u'unsigned',
	                           u'flottant': u'float',
	                           u'double': u'double',
	                           u'vide': u'void',
	                           u'entier 8': u'int8_t',
	                           u'entier 16': u'int16_t',
	                           u'entier 32': u'int32_t',
	                           u'entier 64': u'int64_t',
	                           u'non signé 8': u'uint8_t',
	                           u'non signé 16': u'uint16_t',
	                           u'non signé 32': u'uint32_t',
	                           u'non signé 64': u'uint64_t',
	                         }
	                )
	]

	def _process_recognition(self, node, extras):
		action = Text(extras[u'nom'])
		action.execute()


class ChepRetour(CompoundRule):
	spec = u'retour <valeur>'
	extras = [Choice(u'valeur', { u'vrai': u'true',
	                           u'faux': u'false',
	                         }
	                )
	]

	def _process_recognition(self, node, extras):
		action = Text(u'return ' + extras[u'valeur'] + ';')
		action.execute()


class ChepDivers(MappingRule):
	mapping = {
		u'const': Text(u'const'),
		u'créer en tête': Key(u'cs-f1'),
		u'inclusion chevron': Text(u'inc') + Key(u'tab, tab') + Text(u'<') + Key(u'tab, enter'),
		u'inclusion guillemet': Text(u'inc') + Key(u'tab, tab') + Text(u'"') + Key(u'tab, enter'),
		u'lance': Text(u'throw'),
		u'différent': Text(u' != '),
		u'vrai': Text(u'true'),
		u'faux': Text(u'false'),

		u'pointeur nul': Text(u'nullptr'),
	}


class ChepStandard(MappingRule):
	mapping = {
		u'std': Text(u'std::'),
		u'endl': Text(u'std::endl'),
		u'string': Text(u'std::string'),
		u'console out': Text(u'std::cout<<'),
		u'console erreur': Text(u'std::cerr<<'),
	}


def grammaireCPlusPlus():
	grammarCpp = Grammar('Grammaire C++')
	grammarCpp.add_rule(ChepBlocks())
	grammarCpp.add_rule(ChepClasses())
	grammarCpp.add_rule(ChepVariable())
	grammarCpp.add_rule(ChepType())
	grammarCpp.add_rule(ChepRetour())
	grammarCpp.add_rule(ChepDivers())
	grammarCpp.add_rule(ChepStandard())
	return grammarCpp;


