#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

grammar = Grammar(u'Grammaire Chep')

class ChepGeneral(MappingRule):
	mapping = {
		u'dis <text>': Text(u'%(text)s'),
		u'dit <text>': Text(u'%(text)s'),
		u'demande <text>': Text(u'%(text)s?'),
		u'nombre <n>': Text(u'%(n)d'),
		u'camion': Text(u'pouet pouet'),
		u'controlu [<text>]': Key(u'c-u') + Text(u'%(text)s'),
		u'argument <n>': Key(u'c-u') + Text(u'%(n)d'),
		u'<n> fois <text>': Mimic(extra='text') * Repeat(extra='n'),
		u'Alt tab': Key(u'a-tab'),
		u'loque écran': Key(u'ca-l'),
		u'control c\'est': Key(u'c-c'),
		u'control air': Key(u'c-r'),
		u'tilde': Key(u'tilde'),
		u'alt air': Key(u'a-r'),
		u'alt': Key(u'alt:down'),
		u'control': Key(u'ctrl:down'),
		u'Shift': Key(u'shift:down'),
		u'relâche': Key(u'alt:up,ctrl:up,shift:up'),
	}
	extras = [
		Dictation(u'text'),
		Integer('n', 0, 10000000),
	]
	defaults = {
		'n': 1,
	}


class ChepBuffers(MappingRule):
	mapping = {
		u'fenêtre droite': Key(u'c-c,right'),
		u'fenêtre gauche': Key(u'c-c,left'),
		u'fenêtre haut': Key(u'c-c,up'),
		u'fenêtre bas': Key(u'c-c,down'),
		u'fenêtre suivante': Key(u'c-x,o'),
		u'buffer précédent': Key(u'c-x,left'),
		u'buffer suivant': Key(u'c-x,right'),

		u'bureau suivant': Key(u'c-rangle'),
		u'bureau précédent': Key(u'c-langle'),
		u'nouveau bureau': Key(u'c-c,c-d,a'),
		u'supprime bureau': Key(u'c-c,c-d,d'),
		u'echange bureau': Key(u'c-c,c-d,s'),
		u'bureau numéro <n>': Key(u'a-colon') + Text(u'(virtual-desktops-goto ') + Text(u'%(n)d') + Text(u')') + Key(u'enter'),

		u'split horizontal': Key(u'c-x,3'),
		u'split vertical': Key(u'c-x,2'),
		u'fenêtre unique': Key(u'c-x,1'),
		u'fermer fenêtre': Key(u'c-x,0'),

		u'liste buffer': Key(u'c-x,c-b'),
		u'change buffer': Key(u'c-x,b'),
		u'place ancre [<n>]': Key(u'a-colon') + Text(u'(chep-anchor-place %(n)d)') + Key(u'enter'),
		u'ancre [<n>]': Key(u'a-colon') + Text(u'(chep-anchor-go %(n)d)') + Key(u'enter'),

		u'buffer scratch': Key(u'a-colon') + Text(u'(switch-to-buffer "*scratch*")') + Key(u'enter'),
	}
	extras = [
		Dictation(u'text'),
		IntegerRef('n', 0, 1000),
	]
	defaults = {
		'n': 1,
	}

class ChepAide(MappingRule):
	mapping = {
		u'aide fonction': Key(u'c-h,f'),
		u'aide variable': Key(u'c-h,v'),
		u'aide touche': Key(u'c-h,k'),
	}

class ChepSymboles(MappingRule):
	mapping = {
		u'espace': Key(u'space'),
		u'escape': Key(u'escape'),
		u'tab': Key(u'tab'),
		u'caractère tab': Key(u'c-q,tab'),
		u'entrer': Key(u'enter'),
		u'ligne vide': Key(u'c-j'),
		u'efface': Key(u'backspace'),
		u'supprime': Key(u'del'),
		u'accolade': Key(u'lbrace,rbrace,left'),
		u'ouvre accolade': Key(u'lbrace'),
		u'ferme accolade': Key(u'rbrace'),
		u'parenthèse': Key(u'lparen,rparen,left'),
		u'ouvre parenthèse': Key(u'lparen'),
		u'ferme parenthèse': Key(u'rparen'),
		u'crochet': Key(u'lbracket,rbracket,left'),
		u'ouvre crochet': Key(u'lbracket'),
		u'ferme crochet': Key(u'rbracket'),
		u'deux points': Key(u'colon'),
		u'virgule': Key(u'comma'),
		u'point virgule': Key(u'semicolon'),
		u'point': Key(u'dot'),
		u'point point': Key(u'dot, dot'),
		u'point slash': Key(u'dot, slash'),
		u'point point slash': Key(u'dot, dot, slash'),
		u'dièse': Key(u'hash'),
		u'pourcent': Key(u'percent'),
		u'plus simple': Key(u'plus'),
		u'moins simple': Key(u'minus'),
		u'multiplier simple': Key(u'asterisk'),
		u'dollar': Key(u'dollar'),
		u'étoile': Key(u'asterisk'),
		u'slash': Key(u'slash'),
		u'antislash': Key(u'backslash'),
		u'apostrophe': Key(u'apostrophe'),
		u'quote': Key(u'apostrophe,apostrophe,left'),
		u'double quote': Key(u'dquote,dquote,left'),
		u'guillemets': Key(u'dquote'),
		u'supérieur': Key(u'rangle'),
		u'inférieur': Key(u'langle'),
		u'égal simple': Key(u'equal'),
		u'égal égal': Key(u'space, equal, equal, space'),
		u'exclamation': Key(u'exclamation'),
		u'not': Key(u'exclamation'),
		u'interrogation': Key(u'question'),
		u'paillpe': Key(u'bar'),
		u'underscore': Key(u'underscore'),
		u'et commercial': Key(u'ampersand'),
		u'double et': Key(u'space, ampersand, ampersand, space'),
		u'double ou': Key(u'space, bar, bar, space'),
		u'flèche': Key(u'minus,rangle'),
		u'arobase': Key(u'at'),
		u'plus égal': Key(u'space, plus, equal, space'),
		u'moins égal': Key(u'space, minus, equal, space'),
		u'plus plus': Key(u'plus, plus'),
		u'égal': Key(u'space, equal, space'),
		u'plus': Key(u'space, plus, space'),
		u'moins': Key(u'space, minus, space'),
		u'multiplier': Key(u'space, asterisk, space'),
		u'diviser': Key(u'space, slash, space'),
		u'chevron': Key(u'langle, rangle, left'),

	}


class ChepActions(MappingRule):
	mapping = {
		u'initialise': Key(u'a-x') + Text(u'chep-init-all') + Key(u'enter'),
		u'ouvre': Key(u'c-x,c-f'),
		u'ferme': Key(u'c-x,k'),
		u'controlef': Key(u'c-f'),
		u'enregistre': Key(u'c-x,c-s'),
		u'enregistre tout': Key(u'c-x,s'),
		u'annule': Key(u'c-x,u'),
		u'échappe': Key(u'c-g'),
		u'commande': Key(u'a-x'),
		u'suivant': Key(u'c-s'),
		u'précédent': Key(u'c-r'),
		u'cherche': Key(u'c-s'),
		u'cherche arrière': Key(u'c-r'),
		u'cherche mot': Key(u'c-w'),
		u'remplace': Key(u'a-percent'),
		u'ouvre url': Key(u'c-enter'),
		u'google': Key(u'a-x') + Text(u'google-search-x-browser-region') + Key(u'enter'),
		u'compile': Key(u'a-x') + Text(u'compile') + Key(u'enter'),
		u'agenda': Key(u'c-c,a,n'),
		u'calendrier': Key(u'a-x') + Text(u'calendar') + Key(u'enter'),
		u'speedbar': Key(u'a-x') + Text(u'sr-speedbar-toggle') + Key(u'enter'),
		u'manuel': Key(u'a-x') + Text(u'man') + Key(u'enter'),
	}

class ChepCommandes(MappingRule):
	mapping = {
		u'grep': Key(u'a-x') + Text(u'grep') + Key(u'enter'),
	}


class ChepDeplacements(MappingRule):
	mapping = {
		u'droite': Key(u'right'),
		u'gauche': Key(u'left'),
		u'haut': Key(u'up'),
		u'bas': Key(u'down'),

		u'page bas': Key(u'pgdown'),
		u'page haut': Key(u'pgup'),

		u'fin de ligne': Key(u'c-e'),
		u'début': Key(u'c-a'),

		u'mot droite': Key(u'c-right'),
		u'mot gauche': Key(u'c-left'),

		u'paragraphe haut': Key(u'c-up'),
		u'paragraphe bas': Key(u'c-down'),

		u'début buffer': Key(u'a-langle'),
		u'fin buffer': Key(u'a-rangle'),

		u'ligne': Key(u'a-g,a-g'),

		u'correspondance': Key(u'a-x') + Text('chep-correspondance') + Key('enter'),

		u'fonction suivante':   Key(u'ac-e'),
		u'fonction précédente':  Key(u'ac-a'),
	}

class ChepManipulation(MappingRule):
	mapping = {
		u'sélection': Key(u'c-space'),
		u'sélection rectangle': Key(u'c-x,space'),

		u'copie': Key(u'a-w'),
		u'coupe': Key(u'c-w'),
		u'colle': Key(u'c-y'),
		u'colle colle': Key(u'c-y,c-y'),
		u'colle précédent': Key(u'a-y'),
		u'colle suivant': Key(u'ca-y'),
		u'col précédent': Key(u'a-y'),
		u'col suivant': Key(u'ca-y'),
		u'kill': Key(u'c-k'),
		u'qu\'il': Key(u'c-k'),
		u'kill kill': Key(u'c-k,c-k'),
		u'qu\'il qu\'il': Key(u'c-k,c-k'),

		u'efface mot': Key(u'a-backspace'),
		u'supprime mot': Key(u'c-del'),

		u'échange': Key(u'c-t'),
		u'échange mot': Key(u'a-t'),
	}

class ChepTexte(MappingRule):
	mapping = {
		u'capital': Key(u'a-c'),
		u'minuscule': Key(u'a-l'),
		u'majuscule': Key(u'a-u'),
		u'insertion rectangle': Key(u'a-x') + Text(u'string-rectangle') + Key(u'enter'),
	}

class ChepDivers(MappingRule):
	mapping = {
		u'musique': Key(u'f9'),
		u'musique lecture': Key(u'a-x') + Text(u'chep-mpd-play') + Key('enter'),
		u'musique stop': Key(u'a-x') + Text(u'chep-mpd-stop') + Key('enter'),
		u'musique pause': Key(u'a-x') + Text(u'chep-mpd-pause') + Key('enter'),
		u'terminal': Key(u'f12'),
		u'bonjour irc': Key(u'a-x') + Text(u'chep-erc-bonjour') + Key('enter'),
	}


class ChepLettres(MappingRule):
	mapping = {
		u'alpha': Key(u'a'),
		u'bravo': Key(u'b'),
		u'charlie': Key(u'c'),
		u'delta': Key(u'd'),
		u'echo': Key(u'e'),
		u'foxtrot': Key(u'f'),
		u'golf': Key(u'g'),
		u'hotel': Key(u'h'),
		u'india': Key(u'i'),
		u'juliette': Key(u'j'),
		u'kilo': Key(u'k'),
		u'lima': Key(u'l'),
		u'mike': Key(u'm'),
		u'november': Key(u'n'),
		u'oscar': Key(u'o'),
		u'papa': Key(u'p'),
		u'quebec': Key(u'q'),
		u'romeo': Key(u'r'),
		u'sierra': Key(u's'),
		u'tango': Key(u't'),
		u'uniform': Key(u'u'),
		u'victor': Key(u'v'),
		u'whiskey': Key(u'w'),
		u'xavier': Key(u'x'),
		u'yvonne': Key(u'y'),
		u'zulu': Key(u'z'),
		u'grand alpha': Key(u'A'),
		u'grand bravo': Key(u'B'),
		u'grand charlie': Key(u'C'),
		u'grand delta': Key(u'D'),
		u'grand echo': Key(u'E'),
		u'grand foxtrot': Key(u'F'),
		u'grand golf': Key(u'G'),
		u'grand hotel': Key(u'H'),
		u'grand india': Key(u'I'),
		u'grand juliette': Key(u'J'),
		u'grand kilo': Key(u'K'),
		u'grand lima': Key(u'L'),
		u'grand mike': Key(u'M'),
		u'grand november': Key(u'N'),
		u'grand oscar': Key(u'O'),
		u'grand papa': Key(u'P'),
		u'grand quebec': Key(u'Q'),
		u'grand romeo': Key(u'R'),
		u'grand sierra': Key(u'S'),
		u'grand tango': Key(u'T'),
		u'grand uniform': Key(u'U'),
		u'grand victor': Key(u'V'),
		u'grand whiskey': Key(u'W'),
		u'grand xavier': Key(u'X'),
		u'grand yvonne': Key(u'Y'),
		u'grand zulu': Key(u'Z'),
		u'control alpha': Key(u'c-a'),
		u'control bravo': Key(u'c-b'),
		u'control charlie': Key(u'c-c'),
		u'control delta': Key(u'c-d'),
		u'control echo': Key(u'c-e'),
		u'control foxtrot': Key(u'c-f'),
		u'control golf': Key(u'c-g'),
		u'control hotel': Key(u'c-h'),
		u'control india': Key(u'c-i'),
		u'control juliette': Key(u'c-j'),
		u'control kilo': Key(u'c-k'),
		u'control lima': Key(u'c-l'),
		u'control mike': Key(u'c-m'),
		u'control november': Key(u'c-n'),
		u'control oscar': Key(u'c-o'),
		u'control papa': Key(u'c-p'),
		u'control quebec': Key(u'c-q'),
		u'control romeo': Key(u'c-r'),
		u'control sierra': Key(u'c-s'),
		u'control tango': Key(u'c-t'),
		u'control uniform': Key(u'c-u'),
		u'control victor': Key(u'c-v'),
		u'control whiskey': Key(u'c-w'),
		u'control xavier': Key(u'c-x'),
		u'control yvonne': Key(u'c-y'),
		u'control zulu': Key(u'c-z'),
		u'alt alpha': Key(u'a-a'),
		u'alt bravo': Key(u'a-b'),
		u'alt charlie': Key(u'a-c'),
		u'alt delta': Key(u'a-d'),
		u'alt echo': Key(u'a-e'),
		u'alt foxtrot': Key(u'a-f'),
		u'alt golf': Key(u'a-g'),
		u'alt hotel': Key(u'a-h'),
		u'alt india': Key(u'a-i'),
		u'alt juliette': Key(u'a-j'),
		u'alt kilo': Key(u'a-k'),
		u'alt lima': Key(u'a-l'),
		u'alt mike': Key(u'a-m'),
		u'alt november': Key(u'a-n'),
		u'alt oscar': Key(u'a-o'),
		u'alt papa': Key(u'a-p'),
		u'alt quebec': Key(u'a-q'),
		u'alt romeo': Key(u'a-r'),
		u'alt sierra': Key(u'a-s'),
		u'alt tango': Key(u'a-t'),
		u'alt uniform': Key(u'a-u'),
		u'alt victor': Key(u'a-v'),
		u'alt whiskey': Key(u'a-w'),
		u'alt xavier': Key(u'a-x'),
		u'alt yvonne': Key(u'a-y'),
		u'alt zulu': Key(u'a-z'),

	}

grammar.add_rule(ChepGeneral())
grammar.add_rule(ChepDeplacements())
grammar.add_rule(ChepSymboles())
grammar.add_rule(ChepBuffers())
grammar.add_rule(ChepActions())
grammar.add_rule(ChepCommandes())
grammar.add_rule(ChepManipulation())
grammar.add_rule(ChepTexte())
grammar.add_rule(ChepLettres())
grammar.add_rule(ChepAide())
grammar.add_rule(ChepDivers())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
