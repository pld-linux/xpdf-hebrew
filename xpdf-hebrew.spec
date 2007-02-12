Summary:	ISO-8859-8 and Windows-1255 encoding support for xpdf
Summary(pl.UTF-8):   Wsparcie kodowania ISO-8859-8 i Windows-1255 dla xpdf
Name:		xpdf-hebrew
Version:	1.0
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
# Source0-md5:	438dd417517641cbb78a94facf2d938e
URL:		http://www.foolabs.com/xpdf/
Requires(post,preun):	grep
Requires(post,preun):	xpdf
Requires(preun):	fileutils
Requires:	xpdf
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Xpdf language support packages include CMap files, text encodings,
and various other configuration information necessary or useful for
specific character sets. (They do not include any fonts.)
This package provides support files needed to use the Xpdf tools with
Greek PDF files.

%description -l pl.UTF-8
Pakiety wspierające języki Xpdf zawierają pliki CMap, kodowania oraz
różne inne informacje konfiguracyjne niezbędne bądź przydatne przy
określonych zestawach znaków. (Nie zawierają żadnych fontów).
Ten pakiet zawiera pliki potrzebne do używania narzędzi Xpdf z
greckimi plikami PDF.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xpdf

install *.unicodeMap $RPM_BUILD_ROOT%{_datadir}/xpdf

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
if [ ! -f /etc/xpdfrc ]; then
	echo 'unicodeMap	ISO-8859-8	/usr/share/xpdf/ISO-8859-8.unicodeMap' >> /etc/xpdfrc
	echo 'unicodeMap	Windows-1255	/usr/share/xpdf/Windows-1255.unicodeMap' >> /etc/xpdfrc
else
 if ! grep -q 'ISO-8859-8\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	ISO-8859-8	/usr/share/xpdf/ISO-8859-8.unicodeMap' >> /etc/xpdfrc
 fi
 if ! grep -q 'Windows-1255\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	Windows-1255	/usr/share/xpdf/Windows-1255.unicodeMap' >> /etc/xpdfrc
 fi
fi

%preun
if [ "$1" = "0" ]; then
	umask 022
	grep -v 'ISO-8859-8\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
	grep -v 'Windows-1255\.unicodeMap' /etc/xpdfrc.new > /etc/xpdfrc
	rm -f /etc/xpdfrc.new
fi

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
