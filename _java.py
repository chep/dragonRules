#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aenea import *
from dragonfly.engines.backend_natlink.dictation import NatlinkDictationContainer


class ChepTagsJava(MappingRule):
	mapping = {
		u'cherche tag': Key(u'a-x') + Text(u'eclim-java-find-declaration') + Key(u'enter'),
		u'retour tag': Key(u'a-x') + Text(u'pop-tag-mark') + Key(u'enter'),
		u'occurrence': Key(u'a-x') + Text(u'eclim-java-find-references') + Key(u'enter'),
		u'complétion': Key(u'c-tab'),
		u'compile': Key(u'a-x') + Text(u'eclim-ant-run') + Key(u'enter'),
	}

def grammaireJava():
	grammarCpp = Grammar('Grammaire Java')
	grammarCpp.add_rule(ChepTagsJava())
	return grammarCpp;
