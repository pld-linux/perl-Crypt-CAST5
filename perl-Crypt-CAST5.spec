#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	CAST5
Summary:	Crypt::CAST5 - CAST5 block cipher implementation in C
Summary(pl):	Crypt::CAST5 - implementacja szyfru blokowego CAST5 w C
Name:		perl-Crypt-CAST5
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	79806329ad2f39d31e6770a55a89e199
%{?with_tests:BuildRequires:	perl-Test-Simple >= 0.47}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides an implementation of the CAST5 block cipher using
compiled C code for increased speed. CAST5 is also known as CAST-128.
It is a product of the CAST design procedure developed by C. Adams and
S. Tavares.

%description -l pl
Ten modu³ zawiera implementacjê szyfru blokowego CAST5 w postaci
skompilowanego kodu C, aby zapewniæ wiêksz± szybko¶æ. CAST5 jest znany
tak¿e jako CAST-128. Jest to produkt projektu CAST tworzonego przez
C. Adamsa i S. Tavaresa.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/CAST5.pm
%dir %{perl_vendorarch}/auto/Crypt/CAST5
%{perl_vendorarch}/auto/Crypt/CAST5/CAST5.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/CAST5/CAST5.so
%{_mandir}/man3/*
