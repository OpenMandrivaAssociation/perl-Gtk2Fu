%define upstream_name    Gtk2Fu
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	GTK2 Forked Ultimate, a powerful layer on top of Gtk2 (forked from ugtk2)
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/D/DA/DAMS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Gtk2)

BuildArch:	noarch

%description
gtk2-fu is a layer on top of perl gtk2, that brings power, simplicity
and speed of development. It brings additional methods to ease the widget
creation among other things. But the most important feature is that it
brings you a lot of derivated methods from existing methods, that does
exactly the same thing, except that ir returns the widget.

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
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.110.0-2mdv2011.0
+ Revision: 654969
- rebuild for updated spec-helper

* Tue Feb 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 510093
- update to 0.11

* Wed Aug 05 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.100.0-1mdv2010.0
+ Revision: 410070
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.10-5mdv2009.0
+ Revision: 257158
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.10-3mdv2008.1
+ Revision: 135846
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 05 2005 Antoine Ginies <aginies@n1.mandriva.com> 0.10-3mdk
- various adjustement

* Sat Nov 05 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.1-2mdk
- Fix BuildRequires

* Sat Nov 05 2005 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.1-1mdk
- First Mandriva package

