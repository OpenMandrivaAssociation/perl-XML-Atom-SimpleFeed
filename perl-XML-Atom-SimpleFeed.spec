%define upstream_name    XML-Atom-SimpleFeed
%define upstream_version 0.86

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	No-fuss generation of Atom syndication feeds
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/XML/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
This module provides a minimal API for generating Atom syndication feeds
quickly and easily. It supports all aspects of the Atom format, but has no
provisions for generating feeds with extension elements.

You can supply strings for most things, and the module will provide useful
defaults. When you want more control, you can provide data structures, as
documented, to specify more particulars.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes META.yml
%{_mandir}/man3/*
%{perl_vendorlib}/XML/

%changelog
* Thu Apr 29 2010 Michael Scherer <misc@mandriva.org> 0.860.0-1mdv2010.1
+ Revision: 541067
- import perl-XML-Atom-SimpleFeed


* Thu Apr 29 2010 cpan2dist 0.86-1mdv
- initial mdv release, generated with cpan2dist
