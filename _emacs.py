#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

grammar = Grammar(u'Grammaire Emacs')

class EmacsBuffers(MappingRule):
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
		u'bureau <n>': Key(u'a-colon') + Text(u'(virtual-desktops-goto ') + Text(u'%(n)d') + Text(u')') + Key(u'enter'),

		u'split horizontal': Key(u'c-x,3'),
		u'split vertical': Key(u'c-x,2'),
		u'répartis fenêtres': Key(u'c-x,plus'),
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

class EmacsAide(MappingRule):
	mapping = {
		u'aide fonction': Key(u'c-h,f'),
		u'aide variable': Key(u'c-h,v'),
		u'aide touche': Key(u'c-h,k'),
		u'aide mode': Key(u'c-h,m'),
	}

class EmacsActions(MappingRule):
	mapping = {
		u'initialise': Key(u'a-x') + Text(u'chep-init-all') + Key(u'enter'),
		u'ouvre': Key(u'c-x,c-f'),
		u'ferme': Key(u'c-x,k'),
		u'controlef': Key(u'c-f'),
		u'enregistre': Key(u'c-x,c-s'),
		u'enregistre tout': Key(u'c-x,s'),
		u'enregistre sous': Key(u'c-x,c-w'),
		u'envoie': Key(u'c-c,c-c'),
		u'annule': Key(u'c-x,u'),
		u'échappe': Key(u'c-g'),
		u'commande': Key(u'a-x'),
		u'suivant': Key(u'c-s'),
		u'précédent': Key(u'c-r'),
		u'cherche texte': Key(u'c-s'),
		u'cherche arrière': Key(u'c-r'),
		u'cherche mot': Key(u'c-w'),
		u'remplace': Key(u'a-percent'),
		u'remplace regexp': Key(u'a-x') + Text(u'query-replace-regexp') + Key(u'enter'),
		u'ouvre url': Key(u'c-enter'),
		u'recherche web': Key(u'ws-s'),
		u'agenda': Key(u'c-c,a,n'),
		u'calendrier': Key(u'a-x') + Text(u'calendar') + Key(u'enter'),
		u'speedbar': Key(u'a-x') + Text(u'sr-speedbar-toggle') + Key(u'enter'),
		u'manuel': Key(u'a-x') + Text(u'man') + Key(u'enter'),
	}

class EmacsCommandes(MappingRule):
	mapping = {
		u'grep': Key(u'a-x') + Text(u'grep') + Key(u'enter'),
	}


class EmacsDeplacements(MappingRule):
	mapping = {
		u'droite': Key(u'right'),
		u'gauche': Key(u'left'),
		u'haut': Key(u'up'),
		u'bas': Key(u'down'),

		u'page bas': Key(u'pgdown'),
		u'page haut': Key(u'pgup'),

		u'fin': Key(u'c-e'),
		u'début': Key(u'c-a'),

		u'mot droite': Key(u'c-right'),
		u'mot gauche': Key(u'c-left'),

		u'paragraphe haut': Key(u'c-up'),
		u'paragraphe bas': Key(u'c-down'),

		u'début buffer': Key(u'a-langle'),
		u'fin buffer': Key(u'a-rangle'),

		u'numéro de ligne': Key(u'a-g,a-g'),

		u'correspondance': Key(u'a-x') + Text('chep-correspondance') + Key('enter'),

		u'fonction suivante':   Key(u'ac-e'),
		u'fonction précédente':  Key(u'ac-a'),

		u'déplacement': Key(u'cs-j'),
	}

class EmacsManipulation(MappingRule):
	mapping = {
		u'sélection': Key(u'c-space'),
		u'sélection rectangle': Key(u'c-x,space'),
		u'sélection bloc': Key(u'c-asterisk'),
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

		u'échange lettre': Key(u'c-t'),
		u'échange mot': Key(u'a-t'),
	}

class EmacsCurseur(MappingRule):
	mapping = {
		u'multiples curseurs' : Key(u'c-c,c-m,c-l'),
		u'multiples curseurs mot' : Key(u'c-c,c-m,c-w'),
	}

class EmacsTexte(MappingRule):
	mapping = {
		u'capital': Key(u'a-c'),
		u'minuscule': Key(u'a-l'),
		u'majuscule': Key(u'a-u'),
		u'change casse': Key(u'c-c,i'),
		u'insertion rectangle': Key(u'a-x') + Text(u'string-rectangle') + Key(u'enter'),
	}

class EmacsDivers(MappingRule):
	mapping = {
		u'musique': Key(u'f9'),
		u'musique lecture': Key(u'a-x') + Text(u'emms-play') + Key('enter'),
		u'musique stop': Key(u'a-x') + Text(u'emms-stop') + Key('enter'),
		u'musique pause': Key(u'a-x') + Text(u'emms-pause') + Key('enter'),
		u'terminal': Key(u'f12'),
		u'bonjour tout le monde': Key(u'a-x') + Text(u'chep-erc-bonjour') + Key('enter'),
		u'correction auto': Key(u'a-x') + Text(u'flyspell-auto-correct-word') + Key('enter'),
		u'choix correction': Key(u'a-x') + Text(u'ispell-word') + Key('enter'),
	}


grammar.add_rule(EmacsDeplacements())
grammar.add_rule(EmacsBuffers())
grammar.add_rule(EmacsActions())
grammar.add_rule(EmacsCommandes())
grammar.add_rule(EmacsManipulation())
grammar.add_rule(EmacsCurseur())
grammar.add_rule(EmacsTexte())
grammar.add_rule(EmacsAide())
grammar.add_rule(EmacsDivers())

grammar.load()

def unload():
	global grammar
	if grammar:
		grammar.unload()
	grammar = None
