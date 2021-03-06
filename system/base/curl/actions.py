#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.sub("-D_FORTIFY_SOURCE=\d", "")
    autotools.autoreconf("-fi")
    autotools.configure("--disable-static \
                         --disable-dependency-tracking \
                         --disable-ldap \
                         --disable-ldaps \
                         --with-ssl \
                         --with-zlib \
                         --with-libidn \
                         --with-libssh2 \
                         --without-librtmp \
                         --enable-ipv6 \
                         --enable-http \
                         --enable-ftp \
                         --enable-file \
                         --enable-dict \
                         --enable-manual \
                         --enable-gopher \
                         --enable-telnet \
                         --enable-largefile \
                         --enable-nonblocking \
                         --enable-threaded-resolver \
                         --enable-hidden-symbols \
                         --disable-versioned-symbols \
                         --with-ca-bundle=/etc/ssl/certs/ca-certificates.crt")

def build():
    autotools.make()

def check():
    #shelltools.export("LD_LIBRARY_PATH", "%s/lib" % get.curDIR())
    #autotools.make("-C tests test")
    pass

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("CHANGES", "docs/FEATURES", "docs/MANUAL", "docs/FAQ", "docs/BUGS")
