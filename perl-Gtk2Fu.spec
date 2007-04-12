%define realname   Gtk2Fu

Name:		perl-%{realname}
Version:    0.10
Release:    %mkrel 3
License:	GPL
Group:		Development/Perl
Summary:    GTK2 Forked Ultimate, a powerful layer on top of Gtk2. (forked from ugtk2.)
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DAMS/Gtk2Fu-0.10.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel, perl-Gtk2
BuildArch: noarch

%description
gtk2-fu is a layer on top of perl gtk2, that brings power, simplicity
and speed of development. It brings additional methods to ease the widget
creation among other things. But the most important feature is that it
brings you a lot of derivated methods from existing methods, that does
exactly the same thing, except that ir returns the widget.

%prep
%setup -q -n Gtk2Fu-0.10 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/*
%{_mandir}/man3/*

