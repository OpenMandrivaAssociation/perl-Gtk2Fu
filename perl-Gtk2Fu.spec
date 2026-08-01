%define upstream_name    Gtk2Fu
%define upstream_version 0.11
Name:		perl-%{upstream_name}
Version:	0.11
Release:	3

Summary:	GTK2 Forked Ultimate, a powerful layer on top of Gtk2 (forked from ugtk2)
License:	GPL
Group:		Development/Perl
Url:		https://metacpan.org/dist/Gtk2Fu
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAMS/Gtk2Fu-0.11.tar.gz

BuildRequires:	make
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
%setup -q -n Gtk2Fu-0.11

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
make test || :
%make test || :

%install
%makeinstall_std

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*


