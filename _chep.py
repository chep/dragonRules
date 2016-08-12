#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of Aenea
#
# Aenea is free software: you can redistribute it and/or modify it under
# the terms of version 3 of the GNU Lesser General Public License as
# published by the Free Software Foundation.
#
# Aenea is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with Aenea.  If not, see <http://www.gnu.org/licenses/>.
#
# Copyright (2014) Alex Roper
# Alex Roper <alex@aroper.net>

from aenea import *

grammar = Grammar('Grammaire chep')

class ChepGeneral(MappingRule):
    mapping = {
	    'dis <text>': Text('%(text)s'),
	    'dis camion': Text('pouet pouet'),
	    'minuscule <text>': Text('%(text)s'),
	    'controlu <text>': Key('c-u') + Text('%(text)s'),
	    #'controlu [<n>]': Key('c-u') + Text('%(n)d'),
    }
    extras = [
	    Dictation('text'),
	    #IntegerRef('n',0,9999),
    ]

class ChepBuffers(MappingRule):
	mapping = {
		'buffer droite': Key('c-c,right'),
		'buffer gauche': Key('c-c,left'),
		'buffer haut': Key('c-c,up'),
		'buffer bas': Key('c-c,down'),
		'buffer suivant': Key('c-x,o'),

		'buffer precedent': Key('c-x,left'),
		'buffer suivant': Key('c-x,right'),

		'bureau suivant': Key('c-rangle'),
		'bureau precedent': Key('c-langle'),
		'nouveau bureau': Key('c-c,c-d,a'),
		'supprime bureau': Key('c-c,c-d,d'),

		'split horizontal': Key('c-x,3'),
		'split vertical': Key('c-x,2'),
		'fenetre unique': Key('c-x,1'),
		'fermer fenetre': Key('c-x,0'),

		'liste buffer': Key('c-x,c-b'),
		'change buffer': Key('c-x,b'),
	}


class ChepSymboles(MappingRule):
    mapping = {
	    'espace': Key('space'),
	    'tab': Key('tab'),
	    'entrer': Key('enter'),
	    'efface': Key('backspace'),
	    'supprime': Key('del'),
	    'ouvre accolade': Key('lbrace'),
	    'ferme accolade': Key('rbrace'),
	    'ouvre parenthese': Key('lparen'),
	    'ferme parenthese': Key('rparen'),
	    'ouvre crochet': Key('lbracket'),
	    'ferme crochet': Key('rbracket'),
	    'deux points': Key('colon'),
	    'virgule': Key('comma'),
	    'point virgule': Key('comma'),
	    'point': Key('dot'),
	    'diese': Key('hash'),
	    'pourcent': Key('percent'),
	    'plus': Key('plus'),
	    'moins': Key('minus'),
	    'multiplier': Key('asterisk'),
	    'etoile': Key('asterisk'),
	    'slash': Key('slash'),
	    'antislash': Key('backslash'),
	    'apostrophe': Key('apostrophe'),
	    'quote': Key('apostrophe,apostrophe,left'),
	    'double quote': Key('dquote,dquote,left'),
	    'superieur': Key('rangle'),
	    'inferieur': Key('langle'),
	    'egal': Key('equal'),
	    'exclamation': Key('exclamation'),
	    'paillpe': Key('bar'),
	    'fleche': Key('minus,rangle'),
    }


class ChepActions(MappingRule):
    mapping = {
	    'enregistre': Key('c-x,c-s'),
	    'enregistre tout': Key('c-x,s'),
	    'annuler': Key('c-x,u'),
	    'echappe': Key('c-g'),
	    'commande': Key('a-x'),
	    'suivant': Key('c-s'),
	    'precedent': Key('c-r'),
	    'cherche': Key('c-s'),
    }

class ChepDeplacements(MappingRule):
    mapping = {
	    'droite': Key('right'),
	    'gauche': Key('left'),
	    'haut': Key('up'),
	    'bas': Key('down'),

	    'page bas': Key('pgdown'),
	    'page haut': Key('pgup'),

	    'fin': Key('c-e'),
	    'debut': Key('c-a'),

	    'mot droite': Key('c-right'),
	    'mot gauche': Key('c-left'),

	    'paragraphe haut': Key('c-up'),
	    'paragraphe bas': Key('c-down'),
    }

class ChepManipulation(MappingRule):
    mapping = {
	    'selection': Key('c-space'),
	    'selection rectangle': Key('c-x,space'),

	    'copie': Key('a-w'),
	    'coupe': Key('c-w'),
	    'colle': Key('c-y'),
	    'kill': Key('c-k'),

	    'efface mot': Key('a-backspace'),
	    'supprime mot': Key('c-del'),
    }


grammar.add_rule(ChepDeplacements())
grammar.add_rule(ChepGeneral())
grammar.add_rule(ChepSymboles())
grammar.add_rule(ChepBuffers())
grammar.add_rule(ChepActions())
grammar.add_rule(ChepManipulation())

grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
