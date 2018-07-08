#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Getopt-Tabular
Version  : 0.3
Release  : 1
URL      : https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-0.3.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GW/GWARD/Getopt-Tabular-0.3.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgetopt-tabular-perl/libgetopt-tabular-perl_0.3-2.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-Getopt-Tabular-license
Requires: perl-Getopt-Tabular-man

%description
Getopt::Tabular
version 0.2
19 June, 1997
software; you can redistribute it and/or modify it under the same terms as
Perl itself.

%package license
Summary: license components for the perl-Getopt-Tabular package.
Group: Default

%description license
license components for the perl-Getopt-Tabular package.


%package man
Summary: man components for the perl-Getopt-Tabular package.
Group: Default

%description man
man components for the perl-Getopt-Tabular package.


%prep
tar -xf %{SOURCE1}
cd ..
%setup -q -n Getopt-Tabular-0.3
mkdir -p %{_topdir}/BUILD/Getopt-Tabular-0.3/deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Getopt-Tabular-0.3/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/perl-Getopt-Tabular
cp deblicense/copyright %{buildroot}/usr/share/doc/perl-Getopt-Tabular/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/Getopt/Tabular.pm
/usr/lib/perl5/site_perl/5.26.1/Getopt/Tabular.pod

%files license
%defattr(-,root,root,-)
/usr/share/doc/perl-Getopt-Tabular/deblicense_copyright

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Getopt::Tabular.3
