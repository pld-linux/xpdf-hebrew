Summary:	ISO-8859-8 encoding support for xpdf
Summary(pl):	Wsparcie kodowania ISO-8859-8 dla xpdf
Name:		xpdf-hebrew
Version:	1.0
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.foolabs.com/pub/xpdf/%{name}.tar.gz
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

%description -l pl
Pakiety wspieraj�ce j�zyki Xpdf zawieraj� pliki CMap, kodowania oraz
r�ne inne informacje konfiguracyjne niezb�dne b�d� przydatne przy
okre�lonych zestawach znak�w. (Nie zawieraj� �adnych font�w).
Ten pakiet zawiera pliki potrzebne do u�ywania narz�dzi Xpdf z
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
else
 if ! grep -q 'ISO-8859-8\.unicodeMap' /etc/xpdfrc; then
	echo 'unicodeMap	ISO-8859-8	/usr/share/xpdf/ISO-8859-8.unicodeMap' >> /etc/xpdfrc
 fi
fi

%preun
umask 022
grep -v 'ISO-8859-8\.unicodeMap' /etc/xpdfrc > /etc/xpdfrc.new
mv -f /etc/xpdfrc.new /etc/xpdfrc

%files
%defattr(644,root,root,755)
%doc README add-to-xpdfrc
%{_datadir}/xpdf/*
