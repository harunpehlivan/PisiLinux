#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
    autotools.make()

def install():
    autotools.install()

    pisitools.dohtml("doc/html/*")
    pisitools.dodoc("doc/yasli/*", "README", "CHANGES")
