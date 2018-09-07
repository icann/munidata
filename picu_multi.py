#!/usr/bin/env python

import sys
import os
from picu.loader import icu_load
from picu.constants import U_UNICODE_CHAR_NAME, U_SHORT_PROPERTY_NAME

__version__ = '0.1'
__author__ = 'Wil Tan <wil@cloudregistry.net>'


def main():
    import argparse
    import logging

    parser = argparse.ArgumentParser(description='Test script working with multiple versions of ICU')
    parser.add_argument('-v', '--verbose', action='store_true', help='be verbose')
    parser.add_argument('--libs', action='append', default=[])
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument('codepoint', metavar='CP')
    parser.add_argument('property', metavar='PROP')

    args = parser.parse_args()

    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG if args.verbose else logging.INFO)

    script_name = sys.argv[0]
    if script_name.endswith('.py'):
        script_name = script_name[:-3]
    logger = logging.getLogger(script_name)

    if not args.libs:
        libpath = os.getenv('PICU_ICU_LIB_PATH', '/usr/local/Cellar/icu4c/52.1/lib/libicuuc.52.1.dylib')
        i18n_libpath = os.getenv('PICU_ICU_I18N_LIB_PATH', '/usr/local/Cellar/icu4c/52.1/lib/libicui18n.52.1.dylib')
        libver = os.getenv('PICU_ICU_LIB_VER', '52')
        args.libs.append('{}#{}#{}'.format(libpath, i18n_libpath, libver))

    icu_libs = []
    for libs in args.libs:
        libpath, i18n_libpath, libver = libs.split('#')
        icu = icu_load(libpath, i18n_libpath, libver)
        icu_libs.append(icu)

        logger.info("Library '%s' loaded. Unicode version: %s", libpath, icu.getUnicodeVersion())
        # call the main workhorse function

    if not icu_libs:
        logging.error("No --libs given")
        sys.exit(1)

    cp = int(args.codepoint, 16)
    prop = args.property
    for icu in icu_libs:
        logger.info("Unicode version: %s", icu.getUnicodeVersion())
        print("U+%04X (%s)" % (cp, icu.charName(cp, U_UNICODE_CHAR_NAME)))
        if prop.lower() == 'script_extensions':
            print(icu.get_script_extensions(cp))
        elif prop.lower() == 'script':
            print(icu.get_script(cp))
        elif prop.lower() == 'script_alpha4':
            print(icu.get_script(cp, U_SHORT_PROPERTY_NAME))
        elif prop.lower() == 'age':
            print(icu.charAge(cp))
        else:
            print(icu.get_prop_value(cp, prop))


if __name__ == '__main__':
    main()
