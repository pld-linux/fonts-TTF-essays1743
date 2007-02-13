Summary:	Essays 1743, a font based on an 18th-century typeface
Summary(pl.UTF-8):	Essays 1743 - font oparty na kroju pisma z 18. wieku
Name:		fonts-TTF-essays1743
Version:	1.0
Release:	1
License:	LGPL
Group:		Fonts
Source0:	http://www.thibault.org/fonts/essays/Essays1743-%{version}-ttf.tar.gz
# Source0-md5:	535e9043e006e76929dff127bdc7ffb9
URL:		http://www.thibault.org/fonts/essays/
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Obsoletes:	fonts-ttf-essays1743
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
This is Essays 1743, a font by John Stracke, based on the typeface
used in a 1743 English translation of Montaigne's Essays. The font is
released under the terms of the GNU Lesser General Public License. At
present (version 1.0), it contains normal, bold, italic, and bold
italic versions of 817 characters: all of ASCII, Latin-1, and Latin
Extended A; some of Latin Extended B (basically, the ones that are
more or less based on Roman letters); and a variety of other
characters, such as oddball punctuation, numerals, etc.

%description -l pl.UTF-8
Essays 1743 to font zrobiony przez Johna Stracke, oparty na kroju
pisma użytym w angielskim tłumaczeniu "Esejów" Montaigne'a z 1743 roku.
Font jest wydany na licencji GNU LGPL. Aktualnie (w wersji 1.0)
zawiera normalne, pogrubione, pochyłe i pogrubione pochyłe wersje 817
znaków: całości ASCII, Latin-1 i Latin Extended A; części Latin
Extended B (te mniej lub bardziej oparte na literach łacińskich); oraz
różnych innych znaków, takich jak znaki przestanowe, cyfry itp.

%prep
%setup -q -n Essays1743

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ttffontsdir}
install *.ttf $RPM_BUILD_ROOT%{_ttffontsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc README
%{_ttffontsdir}/*
