#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from aenea import *

class ChepEval(MappingRule):
	mapping = {
		u'évalue région': Key(u'a-x') + Text(u'eval-region') + Key(u'enter'),
		u'évalue buffer': Key(u'a-x') + Text(u'eval-buffer') + Key(u'enter'),
		u'évalue fonction': Key(u'a-x') + Text(u'eval-last-sexp') + Key(u'enter'),
		}

def grammaireLisp():
	grammarLisp = Grammar('Grammaire python')
	grammarLisp.add_rule(ChepEval())
	return grammarLisp