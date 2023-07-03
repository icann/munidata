# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from picu.loader import icu_load
from picu.constants import U_LONG_PROPERTY_NAME, U_SHORT_PROPERTY_NAME
from .idna import idnatables


class UnicodeDatabase(object):
    """
    Base interface and implementation of a Unicode Database.
    """
    def get_unicode_version(self):
        """
        Get the Unicode Version handled by this instance.
        """
        raise NotImplementedError

    def get_char_name(self, cp):
        """
        Retrieve the character's name.

        :param cp: Codepoint.
        :returns: The character's name.
        """
        raise NotImplementedError

    def get_char_age(self, cp):
        """
        Retrieve the character's age.

        :param cp: Codepoint.
        :returns: The character's age.
        """
        raise NotImplementedError

    def get_script(self, cp, alpha4=False):
        raise NotImplementedError

    def get_script_extensions(self, cp, alpha4=False):
        raise NotImplementedError

    def get_prop_value(self, cp, prop_name, prop_type=U_LONG_PROPERTY_NAME):
        raise NotImplementedError

    def is_combining_mark(self, cp):
        """
        Check if character is a combining mark

        :param cp: Codepoint.
        :return:  Whether the character is a combining mark.
        """
        raise NotImplementedError

    def is_digit(self, cp):
        """
        Check if character is a digit.

        :param cp: Codepoint.
        :return:  Whether the character is a digit.
        """
        raise NotImplementedError

    def is_rtl(self, cp):
        """
        Check is character is from a Right To Left script.

        :param cp: Codepoint.
        :return:  Whether the character is from a Right To Left script.
        """
        raise NotImplementedError

    def is_script_rtl(self, script):
        """
        Check is a script is Right To Left.

        :param script: Script.
        :return: Whether the script is Right To Left.
        """
        raise NotImplementedError

    def get_idna_prop(self, cp):
        """
        Retrieve the IDNA property of a character.

        :param cp: Codepoint.
        :returns: IDNA property of the character.
        :raises ValueError: If the Unicode Version is not handled
                            by the IDNA module.
        """
        return idnatables.get_idna_property(cp,
                                            self.get_unicode_version())

    def compile_regex(self, regex):
        """
        Compile a regex.

        :param regex: The regex as a string.
        :return: A regex object, implementation-dependant.
        """
        raise NotImplementedError

    def get_set(self, iterable=None, pattern=None, freeze=False):
        """
        Get a set from given parameters.

        :param iterable: Optional iterable to convert to a set.
        :param pattern: Optional pattern to convert to a set.
        :param freeze: Optional flag to indicate if the set is frozen.
        :return: A set object, implementation-dependant.
        """
        raise NotImplementedError

    def idna_encode(self, input, options=None):
        """
        Encode the given domain name according to the IDNA2008 protocol

        :param input: Unicode string of the domain name to be encoded
        :param options: Optional bitmask options from `picu.constants.UIDNA_*`
        :return: A unicode string representing the result of encoding
        """
        raise NotImplementedError

    def idna_decode(self, input, options=None):
        """
        Decode the given domain name according to the IDNA2008 protocol

        :param input: Unicode string of the domain name to be decoded
        :param options: Optional bitmask options from `picu.constants.UIDNA_*`
        :return: A unicode string representing the result of decoding
        """
        raise NotImplementedError

    def idna_encode_label(self, input, options=None):
        """
        Encode the given domain name label according to the IDNA2008 protocol

        :param input: Unicode string of the domain name label to be encoded
        :param options: Optional bitmask options from `picu.constants.UIDNA_*`
        :return: A unicode string representing the resulting A-label
        """
        raise NotImplementedError

    def idna_decode_label(self, input, options=None):
        """
        Decode the given domain name labelaccording to the IDNA2008 protocol

        :param input: Unicode string of the domain name label to be decoded
        :param options: Optional bitmask options from `picu.constants.UIDNA_*`
        :return: A unicode string representing the resulting U-label
        """
        raise NotImplementedError


class IDNADatabase(UnicodeDatabase):
    """
    Simple implementation that only supports IDNA properties.
    """

    def __init__(self, version):
        self.version = version

    def get_unicode_version(self):
        return self.version


class PICUDatabase(UnicodeDatabase):
    """
    Complete implementation using the PICU python module.
    """

    def __init__(self, icu_uc_lib, icu_i18n_lib, version_tag):
        self._icu = icu_load(icu_uc_lib, icu_i18n_lib, version_tag)

    def get_unicode_version(self):
        return self._icu.getUnicodeVersion()

    def get_char_name(self, cp):
        return self._icu.charName(cp)

    def get_char_age(self, cp):
        return self._icu.charAge(cp)

    def get_script(self, cp, alpha4=False):
        if alpha4:
            prop_type = U_SHORT_PROPERTY_NAME
        else:
            prop_type = U_LONG_PROPERTY_NAME
        return self._icu.get_script(cp, prop_type)

    def is_combining_mark(self, cp):
        return self._icu.is_combining_mark(cp)

    def is_digit(self, cp):
        return self._icu.is_digit(cp)

    def is_rtl(self, cp):
        return self._icu.is_rtl(cp)

    def is_script_rtl(self, script):
        return self._icu.is_script_rtl(script)

    def get_script_extensions(self, cp, alpha4=False):
        if alpha4:
            prop_type = U_SHORT_PROPERTY_NAME
        else:
            prop_type = U_LONG_PROPERTY_NAME
        return self._icu.get_script_extensions(cp, prop_type)

    def get_prop_value(self, cp, prop_name, prop_type=U_LONG_PROPERTY_NAME):
        return self._icu.get_prop_value(cp, prop_name, prop_type)

    def compile_regex(self, regex):
        # return an ICU regex object
        return self._icu.re.compile(regex)

    def get_set(self, iterable=None, pattern=None, freeze=False):
        # return an ICU set object
        return self._icu.set(iterable, pattern, freeze)

    def idna_encode(self, input, options=None):
        return self._icu.idna_encode(input, self._icu.open_uts46(options) if options is not None else None)

    def idna_decode(self, input, options=None):
        return self._icu.idna_decode(input, self._icu.open_uts46(options) if options is not None else None)

    def idna_encode_label(self, input, options=None):
        return self._icu.idna_encode_label(input, self._icu.open_uts46(options) if options is not None else None)

    def idna_decode_label(self, input, options=None):
        return self._icu.idna_decode_label(input, self._icu.open_uts46(options) if options is not None else None)
