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

grammar = Grammar("Grammaire Chep")

class ChepGeneral(MappingRule):
    mapping = {
        'dis <text>': Text(u'%(text)s'),
        'nombre <n>': Text(u'%(n)d'),
        'dis camion': Text(u'pouet pouet'),
        'controlu [<text>]': Key(u'c-u') + Text(u'%(text)s'),
        '<n> fois': Key(u'c-u') + Text(u'%(n)d'),
        'Alt tab': Key(u'a-tab'),
        'loque': Key(u'alt:down,c-l,alt:up'),
    }
    extras = [
        Dictation(u'text'),
        Integer("n", 0, 10000000),
    ]
    defaults = {
        'n': 1,
    }


class ChepBuffers(MappingRule):
    mapping = {
        'buffer droite': Key(u'c-c,right'),
        'buffer gauche': Key(u'c-c,left'),
        'buffer haut': Key(u'c-c,up'),
        'buffer bas': Key(u'c-c,down'),
        'buffer suivant': Key(u'c-x,o'),

        'buffer precedent': Key(u'c-x,left'),
        'buffer suivant': Key(u'c-x,right'),

        'bureau suivant': Key(u'c-rangle'),
        'bureau precedent': Key(u'c-langle'),
        'nouveau bureau': Key(u'c-c,c-d,a'),
        'supprime bureau': Key(u'c-c,c-d,d'),
        'echange bureau': Key(u'c-c,c-d,s'),
        'bureau numero <n>': Key(u'a-colon') + Text(u'(virtual-desktops-goto ') + Text(u'%(n)d') + Text(u')') + Key(u'enter'),

        'split horizontal': Key(u'c-x,3'),
        'split vertical': Key(u'c-x,2'),
        'fenetre unique': Key(u'c-x,1'),
        'fermer fenetre': Key(u'c-x,0'),

        'liste buffer': Key(u'c-x,c-b'),
        'change buffer': Key(u'c-x,b'),
        'place ancre [<n>]': Key(u'c-c,A,P') + Text(u'%(n)d'),
        'ancre [<n>]': Key(u'c-c,A') + Text(u'%(n)d'),

        'buffer scratch': Key(u'a-colon') + Text(u'(switch-to-buffer "*scratch*")') + Key(u'enter'),
    }
    extras = [
        Dictation(u'text'),
        IntegerRef("n", 0, 1000),
    ]
    defaults = {
        'n': 1,
    }

class ChepAide(MappingRule):
    mapping = {
        'aide fonction': Key(u'c-h,f'),
        'aide variable': Key(u'c-h,v'),
        'aide touche': Key(u'c-h,k'),
    }

class ChepSymboles(MappingRule):
    mapping = {
        'espace': Key(u'space'),
        'escape': Key(u'escape'),
        'tab': Key(u'tab'),
        'entrer': Key(u'enter'),
        'efface': Key(u'backspace'),
        'supprime': Key(u'del'),
        'accolade': Key(u'lbrace'),
        'ferme accolade': Key(u'rbrace'),
        'parenthese': Key(u'lparen'),
        'ferme parenthese': Key(u'rparen'),
        'crochet': Key(u'lbracket'),
        'ferme crochet': Key(u'rbracket'),
        'deux points': Key(u'colon'),
        'virgule': Key(u'comma'),
        'point virgule': Key(u'semicolon'),
        'point': Key(u'dot'),
        'diese': Key(u'hash'),
        'pourcent': Key(u'percent'),
        'plus': Key(u'plus'),
        'moins': Key(u'minus'),
        'multiplier': Key(u'asterisk'),
        'etoile': Key(u'asterisk'),
        'slash': Key(u'slash'),
        'antislash': Key(u'backslash'),
        'apostrophe': Key(u'apostrophe'),
        'quote': Key(u'apostrophe,apostrophe,left'),
        'double quote': Key(u'dquote,dquote,left'),
        'superieur': Key(u'rangle'),
        'inferieur': Key(u'langle'),
        'egal': Key(u'equal'),
        'exclamation': Key(u'exclamation'),
        'interrogation': Key(u'question'),
        'paillpe': Key(u'bar'),
        'underscore': Key(u'underscore'),
        'et commercial': Key(u'ampersand'),
        'fleche': Key(u'minus,rangle'),
    }


class ChepActions(MappingRule):
    mapping = {
        'initialise': Key(u'a-x') + Text(u'chep-init-all') + Key(u'enter'),
        'ouvrir': Key(u'c-x,c-f'),
        'fermer': Key(u'c-x,k'),
        'controlef': Key(u'c-f'),
        'enregistre': Key(u'c-x,c-s'),
        'enregistre tout': Key(u'c-x,s'),
        'annuler': Key(u'c-x,u'),
        'echappe': Key(u'c-g'),
        'commande': Key(u'a-x'),
        'suivant': Key(u'c-s'),
        'precedent': Key(u'c-r'),
        'cherche': Key(u'c-s'),
        'cherche arriere': Key(u'c-r'),
        'remplace': Key(u'a-percent'),
        'ouvre url': Key(u'c-enter'),
    }

class ChepDeplacements(MappingRule):
    mapping = {
        'droite': Key(u'right'),
        'gauche': Key(u'left'),
        'haut': Key(u'up'),
        'bas': Key(u'down'),

        'page bas': Key(u'pgdown'),
        'page haut': Key(u'pgup'),

        'fin de ligne': Key(u'c-e'),
        'debut': Key(u'c-a'),

        'mot droite': Key(u'c-right'),
        'mot gauche': Key(u'c-left'),

        'paragraphe haut': Key(u'c-up'),
        'paragraphe bas': Key(u'c-down'),

        'debut buffer': Key(u'a-langle'),
        'fin buffer': Key(u'a-rangle'),

        'ligne': Key(u'a-g,a-g'),
    }

class ChepManipulation(MappingRule):
    mapping = {
        'selection': Key(u'c-space'),
        'selection rectangle': Key(u'c-x,space'),

        'copie': Key(u'a-w'),
        'coupe': Key(u'c-w'),
        'colle': Key(u'c-y'),
        'colle precedent': Key(u'a-y'),
        'colle suivant': Key(u'ctrl:down,a-y,ctrl:up'),
        'kill': Key(u'c-k'),

        'efface mot': Key(u'a-backspace'),
        'supprime mot': Key(u'c-del'),
    }

class ChepTexte(MappingRule):
    mapping = {
        'capital': Key(u'a-c'),
        'minuscule': Key(u'a-l'),
        'majuscule': Key(u'a-u'),
    }

class ChepLettres(MappingRule):
    mapping = {
        'alpha': Key(u'a'),
        'bravo': Key(u'b'),
        'charlie': Key(u'c'),
        'delta': Key(u'd'),
        'echo': Key(u'e'),
        'foxtrot': Key(u'f'),
        'golf': Key(u'g'),
        'hotel': Key(u'h'),
        'india': Key(u'i'),
        'juliette': Key(u'j'),
        'kilo': Key(u'k'),
        'lima': Key(u'l'),
        'mike': Key(u'm'),
        'november': Key(u'n'),
        'oscar': Key(u'o'),
        'papa': Key(u'p'),
        'quebec': Key(u'q'),
        'romeo': Key(u'r'),
        'sierra': Key(u's'),
        'tango': Key(u't'),
        'uniform': Key(u'u'),
        'victor': Key(u'v'),
        'whiskey': Key(u'w'),
        'xavier': Key(u'x'),
        'yvonne': Key(u'y'),
        'zulu': Key(u'z'),
        'grand alpha': Key(u'A'),
        'grand bravo': Key(u'B'),
        'grand charlie': Key(u'C'),
        'grand delta': Key(u'D'),
        'grand echo': Key(u'E'),
        'grand foxtrot': Key(u'F'),
        'grand golf': Key(u'G'),
        'grand hotel': Key(u'H'),
        'grand india': Key(u'I'),
        'grand juliette': Key(u'J'),
        'grand kilo': Key(u'K'),
        'grand lima': Key(u'L'),
        'grand mike': Key(u'M'),
        'grand november': Key(u'N'),
        'grand oscar': Key(u'O'),
        'grand papa': Key(u'P'),
        'grand quebec': Key(u'Q'),
        'grand romeo': Key(u'R'),
        'grand sierra': Key(u'S'),
        'grand tango': Key(u'T'),
        'grand uniform': Key(u'U'),
        'grand victor': Key(u'V'),
        'grand whiskey': Key(u'W'),
        'grand xavier': Key(u'X'),
        'grand yvonne': Key(u'Y'),
        'grand zulu': Key(u'Z'),
    }

grammar.add_rule(ChepGeneral())
grammar.add_rule(ChepDeplacements())
grammar.add_rule(ChepSymboles())
grammar.add_rule(ChepBuffers())
grammar.add_rule(ChepActions())
grammar.add_rule(ChepManipulation())
grammar.add_rule(ChepTexte())
grammar.add_rule(ChepLettres())
grammar.add_rule(ChepAide())

grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
