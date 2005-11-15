#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Size
Summary:	B::Size, B::TerseSize - tools to measure size of Perl OPs and [SAV]Vs
Summary(pl):	B::Size, B::TerseSize - narzêdzia do okre¶lania rozmiaru perlowych OP i [SAV]V
Name:		perl-B-Size
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	efff6c00ac5951c0d5fd76077c580aca
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorarch}/B/*.pm
%dir %{perl_vendorarch}/auto/B
%dir %{perl_vendorarch}/auto/B/Size
%{perl_vendorarch}/auto/B/Size/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/B/Size/*.so
%{_mandir}/man3/*
