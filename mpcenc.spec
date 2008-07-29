Summary:	Musepack encoder
Summary(pl.UTF-8):	Narzędzie do kodowania formatu musepack
Name:		mpcenc
Version:	1.16
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://files.musepack.net/source/mppenc-%{version}.tar.bz2
# Source0-md5:	f1456141283814efcc012cfa15609bc6
URL:		http://www.musepack.net/
BuildRequires:	cmake >= 2.2
BuildRequires:	nasm
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program handles encoding of the MPC format, which is an audio
compression format with a strong emphasis on high quality. It's not
lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much
smaller MPC file. It is based on the MPEG-1 Layer-2 / MP2 algorithms,
but since 1997 it has rapidly developed and vastly improved and is now
at an advanced stage in which it contains heavily optimized and
patentless code.

%description -l pl.UTF-8
Ten program obsługuje kodowanie formatu MPC, który jest formatem
kompresji dźwięku z naciskiem na wysoką jakość. Nie jest bezstratny,
ale jest zaprojektowany dla przezroczystości, tak, że nie można
usłyszeć różnicy między oryginalnym plikiem wave a dużo mniejszym
plikiem MPC. Jest oparty na algorytmach MPEG-1 Layer-2 / MP2, ale od
1997 roku został znacznie rozwinięty i ulepszony, a teraz jest w
zaawansowanym stadium, w którym zawiera silnie zoptymalizowany i nie
objęty patentami kod.

%prep
%setup  -q -n mppenc-%{version}

%build
cd src
%{cmake} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}" \
	.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install src/mppenc $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog
%attr(755,root,root) %{_bindir}/*
