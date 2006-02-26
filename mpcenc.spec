Summary:	Musepack encoder
Summary(pl):	Narzêdzie do kodowania formatu musepack
Name:		mpcenc
Version:	1.15v
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://files2.musepack.net/source/mpcsv7-src-%{version}.tar.bz2
# Source0-md5:	eb3e6b64b1f7d68aaeb04e39936d87fb
URL:		http://www.musepack.net/
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

%description -l pl
Ten program obs³uguje kodowanie formatu MPC, który jest formatem
kompresji d¼wiêku z naciskiem na wysok± jako¶æ. Nie jest bezstratny,
ale jest zaprojektowany dla przezroczysto¶ci, tak, ¿e nie mo¿na
us³yszeæ ró¿nicy miêdzy oryginalnym plikiem wave a du¿o mniejszym
plikiem MPC. Jest oparty na algorytmach MPEG-1 Layer-2 / MP2, ale od
1997 roku zosta³ znacznie rozwiniêty i ulepszony, a teraz jest w
zaawansowanym stadium, w którym zawiera silnie zoptymalizowany i nie
objêty patentami kod.

%prep
%setup -q -n sv7

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mppenc replaygain $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,CHANGES,MANUAL.TXT,TODO}
%attr(755,root,root) %{_bindir}/*
