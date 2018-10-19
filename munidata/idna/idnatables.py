# -*- coding: utf-8 -*-
"""
idnatables.py - Provide access to the data from IANA's IDNA 2008 tables.
"""
from __future__ import unicode_literals

import logging

from .idna_tables_1100 import idna_tables_1100
from .idna_tables_1000 import idna_tables_1000
from .idna_tables_900 import idna_tables_900
from .idna_tables_800 import idna_tables_800
from .idna_tables_700 import idna_tables_700
from .idna_tables_630 import idna_tables_630
from .idna_tables_620 import idna_tables_620
from .idna_tables_610 import idna_tables_610
from .idna_tables_600 import idna_tables_600
from .idna_tables_520 import idna_tables_520

logger = logging.getLogger(__name__)


IDNA_UNICODE_MAPPING = {
    '11.0.0': idna_tables_1100,
    '10.0.0': idna_tables_1000,
    '9.0.0': idna_tables_900,
    '8.0.0': idna_tables_800,
    '7.0.0': idna_tables_700,
    '6.3.0': idna_tables_630,
    '6.2.0': idna_tables_620,
    '6.1.0': idna_tables_610,
    '6.0.0': idna_tables_600,
    '5.2.0': idna_tables_520,
}

IDNA_PROPERTIES = [
    'PVALID',
    'CONTEXTO',
    'CONTEXTJ',
    'DISALLOWED',
    'UNASSIGNED'
]


def get_idna_property(cp, unicode_version='6.3.0'):
    """
    Get the IDNA 2008 properties for a given codepoint.

    :param cp: The codepoint to look for in the IDNA tables.
    :param unicode_version: Unicode version to use.
    :returns: One of the IDNA_PROPERTIES values.
    :raises ValueError: If unicode_version is not handled by any IDNA table.
    """
    if unicode_version not in IDNA_UNICODE_MAPPING.keys():
        logger.error("Invalid Unicode version '%s'", unicode_version)
        raise ValueError("Invalid Unicode version '{0}'".format(unicode_version))

    mapper = IDNA_UNICODE_MAPPING[unicode_version]

    for prop in IDNA_PROPERTIES:
        if prop == 'UNASSIGNED':
            continue
        if cp in mapper[prop]:
            return prop
    return 'UNASSIGNED'
