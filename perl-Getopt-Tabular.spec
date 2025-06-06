#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Getopt-Tabular
Version  : 0.3
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-0.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-0.3.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgetopt-tabular-perl/libgetopt-tabular-perl_0.3-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Getopt-Tabular-license = %{version}-%{release}
Requires: perl-Getopt-Tabular-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Getopt::Tabular
version 0.2
19 June, 1997
software; you can redistribute it and/or modify it under the same terms as
Perl itself.

%package dev
Summary: dev components for the perl-Getopt-Tabular package.
Group: Development
Provides: perl-Getopt-Tabular-devel = %{version}-%{release}
Requires: perl-Getopt-Tabular = %{version}-%{release}

%description dev
dev components for the perl-Getopt-Tabular package.


%package license
Summary: license components for the perl-Getopt-Tabular package.
Group: Default

%description license
license components for the perl-Getopt-Tabular package.


%package perl
Summary: perl components for the perl-Getopt-Tabular package.
Group: Default
Requires: perl-Getopt-Tabular = %{version}-%{release}

%description perl
perl components for the perl-Getopt-Tabular package.


%prep
%setup -q -n Getopt-Tabular-0.3
cd %{_builddir}
tar xf %{_sourcedir}/libgetopt-tabular-perl_0.3-2.debian.tar.xz
cd %{_builddir}/Getopt-Tabular-0.3
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Getopt-Tabular-0.3/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Getopt-Tabular
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Getopt-Tabular/bea1a949258e0c2fb224e563838c4efd303f5c43 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Getopt::Tabular.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Getopt-Tabular/bea1a949258e0c2fb224e563838c4efd303f5c43

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
