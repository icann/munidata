#!/usr/bin/env python

import sys
import os
from munidata import UnicodeDataVersionManager

__version__ = '0.1'
__author__ = 'Wil Tan <wil@cloudregistry.net>'


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Test script working with multiple versions of ICU')
    parser.add_argument('-v', '--verbose', action='store_true', help='be verbose')
    parser.add_argument('--libs', action='append', default=[])
    parser.add_argument('--version', action='version', version='%(prog)s {}'.format(__version__))
    parser.add_argument('codepoint', metavar='CP')
    parser.add_argument('property', metavar='PROP')

    args = parser.parse_args()

    manager = UnicodeDataVersionManager()
    if not args.libs:
        libpath = os.getenv('PICU_ICU_LIB_PATH', '/usr/local/Cellar/icu4c/52.1/lib/libicuuc.52.1.dylib')
        i18n_libpath = os.getenv('PICU_ICU_I18N_LIB_PATH', '/usr/local/Cellar/icu4c/52.1/lib/libicui18n.52.1.dylib')
        libver = os.getenv('PICU_ICU_LIB_VER', '52')
        args.libs.append('{}#{}#{}'.format(libpath, i18n_libpath, libver))

    databases = []
    for libs in args.libs:
        libpath, i18n_libpath, libver = libs.split('#')
        db = manager.register(None, libpath, i18n_libpath, libver)
        databases.append(db)

    if not databases:
        sys.exit(1)

    cp = int(args.codepoint, 16)
    prop = args.property
    for db in databases:
        print("Unicode version: %s" % db.get_unicode_version())
        print("U+%04X (%s)" % (cp, db.get_char_name(cp)))
        if prop.lower() == 'script_extensions':
            print(db.get_script_extensions(cp))
        elif prop.lower() == 'script_alpha4':
            print(db.get_script(cp, alpha4=True))
        elif prop.lower() == 'age':
            print(db.get_char_age(cp))
        else:
            print(db.get_prop_value(cp, prop))

if __name__ == '__main__':
    main()
