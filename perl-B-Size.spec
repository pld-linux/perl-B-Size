#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Size
Summary:	B::Size, B::TerseSize - tools to measure size of Perl OPs and [SAV]Vs
Summary(pl):	B::Size, B::TerseSize - narzêdzia do okre¶lania rozmiaru perlowych OP i [SAV]V
Name:		perl-B-Size
Version:	0.05
Release:	3
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The B::Size and B::TerseSize modules attempt to measure the size of
Perl op codes. The output of B::TerseSize is similar to that of
B::Terse, but includes the size of each OP in the tree and the PADLIST
(subroutine lexical variables). The module can be run just as other
compiler backends or used via Apache::Status (version 2.02 and
higher).

%description -l pl
Modu³y B::Size i B::TerseSize próbuj± okre¶liæ rozmiar perlowych
opkodów. Wyj¶cie B::TerseSize jest podobne do wyj¶cia B::Terse, ale
zawiera rozmiar ka¿dego OP w drzewie oraz PADLIST (leksykalne zmienne
procedur). Modu³ mo¿e byæ uruchamiany tak jak inne backendy
kompilatora lub u¿ywany poprzez Apache::Status (w wersji 2.02 lub
wy¿szej).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitearch}/B/*.pm
%dir %{perl_sitearch}/auto/B
%dir %{perl_sitearch}/auto/B/Size
%{perl_sitearch}/auto/B/Size/*.bs
%attr(755,root,root) %{perl_sitearch}/auto/B/Size/*.so
%{_mandir}/man3/*
