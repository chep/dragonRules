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
        #'controlu <text>': Key('c-u') + Text('%(text)s'),
        'controlu [<n>]': Key('c-u') + Text('%(n)d'),
        '[<n>] fois': Key('c-u') + Text('%(n)d'),
        'Alt tab': Key('a-tab'),
    }
    extras = [
        Dictation('text'),
        Integer("n", 1, 1000),
    ]
    defaults = {
        'n': 1,
    }


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
        'echange bureau': Key('c-c,c-d,s'),

        'split horizontal': Key('c-x,3'),
        'split vertical': Key('c-x,2'),
        'fenetre unique': Key('c-x,1'),
        'fermer fenetre': Key('c-x,0'),

        'liste buffer': Key('c-x,c-b'),
        'change buffer': Key('c-x,b'),
        'place ancre [<n>]': Key('c-c,A,P') + Text('%(n)d'),
        'ancre [<n>]': Key('c-c,A') + Text('%(n)d'),
    }
    extras = [
        Dictation('text'),
        Integer("n", 1, 1000),
    ]
    defaults = {
        'n': 1,
    }


class ChepSymboles(MappingRule):
    mapping = {
        'espace': Key('space'),
        'escape': Key('escape'),
        'tab': Key('tab'),
        'entrer': Key('enter'),
        'efface': Key('backspace'),
        'supprime': Key('del'),
        'accolade': Key('lbrace'),
        'ferme accolade': Key('rbrace'),
        'parenthese': Key('lparen'),
        'ferme parenthese': Key('rparen'),
        'crochet': Key('lbracket'),
        'ferme crochet': Key('rbracket'),
        'deux points': Key('colon'),
        'virgule': Key('comma'),
        'point virgule': Key('semicolon'),
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
	    'interrogation': Key('question'),
        'paillpe': Key('bar'),
	    'underscore': Key('underscore'),
	    'et commercial': Key('ampersand'),
        'fleche': Key('minus,rangle'),
    }


class ChepActions(MappingRule):
    mapping = {
        'initialise': Key('a-x') + Text('chep-init-all') + Key('enter'),
        'ouvrir': Key('c-x,c-f'),
        'fermer': Key('c-x,k'),
        'controlef': Key('c-f'),
        'enregistre': Key('c-x,c-s'),
        'enregistre tout': Key('c-x,s'),
        'annuler': Key('c-x,u'),
        'echappe': Key('c-g'),
        'commande': Key('a-x'),
        'suivant': Key('c-s'),
        'precedent': Key('c-r'),
        'cherche': Key('c-s'),
        'cherche arriere': Key('c-r'),
        'remplace': Key('a-percent'),
    }

class ChepDeplacements(MappingRule):
    mapping = {
        'droite': Key('right'),
        'gauche': Key('left'),
        'haut': Key('up'),
        'bas': Key('down'),

        'page bas': Key('pgdown'),
        'page haut': Key('pgup'),

        'fin de ligne': Key('c-e'),
        'debut': Key('c-a'),

        'mot droite': Key('c-right'),
        'mot gauche': Key('c-left'),

        'paragraphe haut': Key('c-up'),
        'paragraphe bas': Key('c-down'),

        'debut buffer': Key('a-langle'),
        'fin buffer': Key('a-rangle'),
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

class ChepTexte(MappingRule):
    mapping = {
        'capital': Key('a-c'),
        'minuscule': Key('a-l'),
        'majuscule': Key('a-u'),
    }

class ChepLettres(MappingRule):
    mapping = {
        'alpha': Key('a'),
        'bravo': Key('b'),
        'charlie': Key('c'),
        'delta': Key('d'),
        'echo': Key('e'),
        'foxtrot': Key('f'),
        'golf': Key('g'),
        'hotel': Key('h'),
        'india': Key('i'),
        'juliette': Key('j'),
        'kilo': Key('k'),
        'lima': Key('l'),
        'mike': Key('m'),
        'november': Key('n'),
        'oscar': Key('o'),
        'papa': Key('p'),
        'quebec': Key('q'),
        'romeo': Key('r'),
        'sierra': Key('s'),
        'tango': Key('t'),
        'uniform': Key('u'),
        'victor': Key('v'),
        'whiskey': Key('w'),
        'xavier': Key('x'),
        'yvonne': Key('y'),
        'zulu': Key('z'),
        'grand alpha': Key('A'),
        'grand bravo': Key('B'),
        'grand charlie': Key('C'),
        'grand delta': Key('D'),
        'grand echo': Key('E'),
        'grand foxtrot': Key('F'),
        'grand golf': Key('G'),
        'grand hotel': Key('H'),
        'grand india': Key('I'),
        'grand juliette': Key('J'),
        'grand kilo': Key('K'),
	    'grand lima': Key('L'),
        'grand mike': Key('M'),
        'grand november': Key('N'),
        'grand oscar': Key('O'),
        'grand papa': Key('P'),
        'grand quebec': Key('Q'),
        'grand romeo': Key('R'),
        'grand sierra': Key('S'),
        'grand tango': Key('T'),
        'grand uniform': Key('U'),
        'grand victor': Key('V'),
	    'grand whiskey': Key('W'),
        'grand xavier': Key('X'),
        'grand yvonne': Key('Y'),
        'grand zulu': Key('Z'),
    }

grammar.add_rule(ChepDeplacements())
grammar.add_rule(ChepGeneral())
grammar.add_rule(ChepSymboles())
grammar.add_rule(ChepBuffers())
grammar.add_rule(ChepActions())
grammar.add_rule(ChepManipulation())
grammar.add_rule(ChepTexte())
grammar.add_rule(ChepLettres())

grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
