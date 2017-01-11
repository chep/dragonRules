#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer
from _communCode import *

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
		u'fonction': Text(u'mf') + Key(u'tab'),
		u'fonction main': Text(u'main') + Key(u'tab'),
		u'déclaration': Text(u'f') + Key(u'tab'),
		u'privé': Text(u'private:') + Key(u'tab') + Key(u'enter'),
		u'public': Text(u'public:') + Key(u'tab') + Key(u'enter'),
		u'protégé': Text(u'protected:') + Key(u'tab') + Key(u'enter'),
	}


class ChepType(CompoundRule):
	spec = u'type <nom>'
	extras = [Choice(u'nom', { u'entier': u'int ',
	                           u'bool': u'bool ',
	                           u'non signé': u'unsigned ',
	                           u'flottant': u'float ',
	                           u'double': u'double ',
	                           u'char': u'char ',
	                           u'vide': u'void ',
	                           u'entier 8': u'int8_t ',
	                           u'entier 16': u'int16_t ',
	                           u'entier 32': u'int32_t ',
	                           u'entier 64': u'int64_t ',
	                           u'non signé 8': u'uint8_t ',
	                           u'non signé 16': u'uint16_t ',
	                           u'non signé 32': u'uint32_t ',
	                           u'non signé 64': u'uint64_t ',
	                           u'auto': u'auto ',
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
		u'const': Text(u'const '),
		u'créer en tête': Key(u'cs-f1'),
		u'inclusion chevron': Text(u'incs') + Key(u'tab'),
		u'inclusion guillemet': Text(u'incl') + Key(u'tab'),
		u'lance': Text(u'throw'),
		u'différent': Text(u' != '),
		u'vrai': Text(u'true'),
		u'faux': Text(u'false'),

		u'pointeur nul': Text(u'nullptr'),

		u'envoie': Text(u'>>'),
		u'reçoit': Text(u'<<'),
		u'double deux points': Text(u'::'),

		u'compile': Key(u'a-x') + Text(u'compile') + Key(u'enter'),
	}


class ChepStandard(MappingRule):
	mapping = {
		u'std': Text(u'std::'),
		u'endl': Text(u'std::endl'),
		u'string': Text(u'std::string'),
		u'console out': Text(u'std::cout<<'),
		u'console erreur': Text(u'std::cerr<<'),
	}

class ChepTagsPlusPlus(MappingRule):
	mapping = {
		u'cherche tag': Key(u'a-semicolon'),
		u'retour tag': Key(u'a-asterisk'),
		u'info tag': Key(u'ca-semicolon'),
		u'occurrence': Key(u'c-c,r,slash'),
		u'complétion': Key(u'c-tab'),
		u'renomme tag': Key(u'a-x') + Text(u'rtags-rename-symbol') + Key(u'enter'),
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
	grammarCpp.add_rule(ChepTagsPlusPlus())
	return grammarCpp;


