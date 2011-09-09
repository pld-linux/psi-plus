#!/bin/sh

git clone git://git.psi-im.org/psi.git
cd psi
git submodule init
git submodule update
git pull
git submodule update
svn co http://psi-dev.googlecode.com/svn/trunk/patches/
# already applied
rm patches/0005-psi-proxy-settings-in-opt.diff
cat patches/*.diff | patch -p1
pkgrel=`svnversion "patches"`
cd src
sed "s/\(.xxx\)/.${pkgrel}/" -i "applicationinfo.cpp"
cd ..
svn co --force http://psi-dev.googlecode.com/svn/trunk/iconsets/ iconsets
cd ..
mv psi psi-plus-0.15.${pkgrel}
tar -cvJf psi-plus-0.15.${pkgrel}.tar.xz psi-plus-0.15.${pkgrel}
rm -rf psi-plus-0.15.${pkgrel}
