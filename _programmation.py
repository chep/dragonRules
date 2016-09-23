#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *
from _cplusplus import *
from _python import *
from _lisp import *


switcherGrammaire = {
	u'c++': grammaireCPlusPlus(),
	u'python': grammairePython(),
	u'lisp': grammaireLisp(),
}

class Programmation:
	def __init__(self):
		self.grammaire = None

	def charge(self, langage):
		if (self.grammaire):
			self.grammaire.unload()
		self.grammaire = switcherGrammaire.get(langage, None)
		if (self.grammaire):
			self.grammaire.load()

prog = Programmation()


def appelCplusplus():
	prog.charge(u'c++')
def appelPython():
	prog.charge(u'python')
def appelLisp():
	prog.charge(u'lisp')

class ChepProg(MappingRule):
	mapping = {
 		u'programmation C plus plus':Function(appelCplusplus),
 		u'programmation python': Function(appelPython),
 		u'programmation lisp': Function(appelLisp),
 	}


grammarProg = Grammar('Grammaire programmation')
grammarProg.add_rule(ChepProg())
grammarProg.load()

def unload():
	global grammarProg
	if grammarProg:
		grammarProg.unload()
	grammarProg = None
