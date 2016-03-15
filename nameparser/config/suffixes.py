# -*- coding: utf-8 -*-
from __future__ import unicode_literals

SUFFIX_NOT_ACRONYMS = set([
    'esq',
    'esquire',
    'jr',
    'jnr',
    'sr',
    'snr',
    '2',
    'i',
    'ii',
    'iii',
    'iv',
    'v',
])
"""

Post-nominal pieces that are not acronyms. The parser does not remove periods
when matching against these pieces.

"""
SUFFIX_ACRONYMS = set([
    'ae',
    'afc',
    'afm',
    'arrc',
    'bart',
    'bem',
    'bt',
    'cb',
    'cbe',
    'cfp',
    'cgc',
    'cgm',
    'ch',
    'chfc',
    'cie',
    'clu',
    'cmg',
    'cpa',
    'cpm',
    'csi',
    'csm',
    'cvo',
    'dbe',
    'dcb',
    'dcm',
    'dcmg',
    'dcvo',
    'dds',
    'dfc',
    'dfm',
    'dmd',
    'do',
    'dpm',
    'dsc',
    'dsm',
    'dso',
    'dvm',
    'ed',
    'erd',
    'gbe',
    'gc',
    'gcb',
    'gcie',
    'gcmg',
    'gcsi',
    'gcvo',
    'gm',
    'idsm',
    'iom',
    'iso',
    'kbe',
    'kcb',
    'kcie',
    'kcmg',
    'kcsi',
    'kcvo',
    'kg',
    'kp',
    'kt',
    'lg',
    'lt',
    'lvo',
    'ma',
    'mba',
    'mbe',
    'mc',
    'md',
    'mm',
    'mp',
    'msc'
    'msm',
    'mvo',
    'obe',
    'obi',
    'om',
    'phd',
    'phr',
    'pmp',
    'qam',
    'qc',
    'qfsm',
    'qgm',
    'qpm',
    'rd',
    'rrc',
    'rvm',
    'sgm',
    'td',
    'ud',
    'vc',
    'vd',
    'vrd',
])
"""

Post-nominal acronyms. Titles, degrees and other things people stick after their name
that may or may not have periods between the letters. The parser removes periods 
when matching against these pieces.

"""
SUFFIXES = SUFFIX_ACRONYMS | SUFFIX_NOT_ACRONYMS
"""
A union of the sets :py:attr:`SUFFIX_ACRONYMS` and :py:attr:`SUFFIX_NOT_ACRONYMS`
"""
