Summary:	PSI - Jabber client
Summary(de.UTF-8):	PSI - ein Instant Messaging Client-Programm für Jabber
Summary(pl.UTF-8):	PSI - klient Jabbera
Name:		psi-plus
Version:	0.16.470
Release:	2
License:	GPL v2+ / LGPL v2.1+
Group:		Applications/Communications
Source0:	https://github.com/psi-plus/psi-plus-snapshots/archive/%{version}.tar.gz
# Source0-md5:	e5a38d6bb368fa9aaaab6ff02ca154e6
URL:		https://github.com/psi-plus/psi-plus-snapshots
BuildRequires:	Qt3Support-devel
BuildRequires:	QtCore-devel
BuildRequires:	QtDBus-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	QtSvg-devel
BuildRequires:	QtWebKit-devel
BuildRequires:	QtXml-devel
BuildRequires:	aspell-devel
BuildRequires:	libidn-devel
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel >= 0.9.7c
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= 4.4.0
BuildRequires:	qt4-linguist >= 4.4.0
BuildRequires:	qt4-qmake >= 4.4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	which
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXScrnSaver-devel
BuildRequires:	xorg-proto-scrnsaverproto-devel
BuildRequires:	xz >= 1:4.999.7
BuildRequires:	zlib-devel
Requires:	gstreamer-v4l2
Requires:	qt4-plugin-qca-ossl
Suggests:	gpgme >= 1.0.0
Provides:	psi = %{version}-%{relase}
Obsoletes:	psi < 0.16
Obsoletes:	qt-designer-psiwidgets
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PSI is a communicator for the Jabber open messaging system. It is
based on the Qt library. It supports SSL encrypted connections. The
default behaviour for SSL was changed so that it looks for SSL
certificates in $DATADIR/certs or in ~/.psi/certs.

Psi+ is a development branch of Psi IM Jabber client.

%description -l de.UTF-8
Psi ist ein Instant Messaging (IM) Client-Programm für das
Jabber-Protokoll (XMPP), welches das Qt Toolkit nutzt.

%description -l pl.UTF-8
PSI jest komunikatorem dla otwartego systemu wiadomości Jabber. Został
stworzony w oparciu o bibliotekę Qt. PSI wspiera połączenia szyfrowane
SSL. W stosunku do domyślnego zachowania komunikatora została
wprowadzona zmiana, która powoduje, że certyfikaty SSL są poszukiwane
w katalogu $DATADIR/certs lub ~/.psi/certs.

Psi+ jest rozwojową gałęzią komunikatora Psi IM Jabber.

%prep
%setup -q -n %{name}-snapshots-%{version}

%build
./configure \
	--prefix=%{_prefix} \
	--datadir=%{_datadir} \
	--libdir=%{_libdir} \
	--enable-webkit \
	--enable-whiteboarding \
	--enable-plugins \
	--no-separate-debug-info

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

export QTDIR=%{_libdir}/qt4

install -d $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/psi-plus
%{_datadir}/psi
%{_libdir}/psi
%dir %{_libdir}/%{name}/plugins
%{_datadir}/%{name}/certs
%{_datadir}/%{name}/iconsets
%{_datadir}/%{name}/sound
%{_datadir}/%{name}/themes
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
