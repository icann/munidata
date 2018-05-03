# Munidata

munidata is an API for accessing multiple instances of Unicode data.

The current version of munidata is a simple abstraction layer on top of the [picu](https://pypi.python.org/pypi/picu) module.

## Acknowledgment

This toolset was implemented by Viagenie (Audric Schiltknecht, David
Drouin and Marc Blanchet) and Wil Tan on an ICANN contract.

## License

Copyright (c) 2015-2016 Internet Corporation for Assigned Names and
Numbers (“ICANN”). All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of the ICANN nor the names of its contributors
      may be used to endorse or promote products derived from this
      software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY ICANN AND CONTRIBUTORS ``AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL ICANN OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
THE POSSIBILITY OF SUCH DAMAGE.
## Pre-requisites

* Python (2.7, or >= 3.4)
* [picu](https://pypi.python.org/pypi/picu) [MIT/X License]

## Setup

If your distribution does not package the required dependencies, the easiest way
to get a working environment in no-time is to use Python's virtual environments.

* Install [virtualenv](https://github.com/pypa/virtualenv)
* Create a python virtualenv:

		$ virtualenv venv

* Activate the environment:

		$ source ./venv/bin/activate

* Download dependencies:

		$ (venv) pip install -r requirements.txt

* Install some versions of the [ICU library](http://site.icu-project.org/download)

## Use

To get the general category of a codepoint for multiple ICU versions:

    $ python test_munidata.py --libs /usr/local/Cellar/icu4c/52.1/lib/libicuuc.dylib#/usr/local/Cellar/icu4c/52.1/lib/libicui18n.52.1.dylib#52 --libs /usr/local/Cellar/icu4c/4.4.1/lib/libicuuc.dylib#/usr/local/Cellar/icu4c/4.4.1/lib/libicui18n.dylib#44 19DA gc
    Unicode version: %s 6.3.0.0
    U+19DA (NEW TAI LUE THAM DIGIT ONE)
    Other_Number
    Unicode version: %s 5.2.0.0
    U+19DA (NEW TAI LUE THAM DIGIT ONE)
    Decimal_Number

Same thing with just plain picu:

    $ python picu_multi.py --libs /usr/local/Cellar/icu4c/52.1/lib/libicuuc.dylib#/usr/local/Cellar/icu4c/52.1/lib/libicui18n.52.1.dylib#52 --libs /usr/local/Cellar/icu4c/4.4.1/lib/libicuuc.dylib#/usr/local/Cellar/icu4c/4.4.1/lib/libicui18n.dylib#44 19DA gc
    INFO:picu_multi:Library '/usr/local/Cellar/icu4c/52.1/lib/libicuuc.dylib' loaded. Unicode version: 6.3.0.0
    INFO:picu_multi:Library '/usr/local/Cellar/icu4c/4.4.1/lib/libicuuc.dylib' loaded. Unicode version: 5.2.0.0
    INFO:picu_multi:Unicode version: 6.3.0.0
    U+19DA (NEW TAI LUE THAM DIGIT ONE)
    Other_Number
    INFO:picu_multi:Unicode version: 5.2.0.0
    U+19DA (NEW TAI LUE THAM DIGIT ONE)
    Decimal_Number
