#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	B
%define		pnam	Size
Summary:	B::Size, B::TerseSize - tools to measure size of Perl OPs and [SAV]Vs
Summary(pl.UTF-8):	B::Size, B::TerseSize - narzędzia do określania rozmiaru perlowych OP i [SAV]V
Name:		perl-B-Size
Version:	0.09
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/B/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ee8bfb21beccf70621b4750b779795a6
URL:		http://search.cpan.org/dist/B-Size/
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

%description -l pl.UTF-8
Moduły B::Size i B::TerseSize próbują określić rozmiar perlowych
opkodów. Wyjście B::TerseSize jest podobne do wyjścia B::Terse, ale
zawiera rozmiar każdego OP w drzewie oraz PADLIST (leksykalne zmienne
procedur). Moduł może być uruchamiany tak jak inne backendy
kompilatora lub używany poprzez Apache::Status (w wersji 2.02 lub
wyższej).

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
