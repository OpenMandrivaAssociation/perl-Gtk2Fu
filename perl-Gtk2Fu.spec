%define upstream_name    Gtk2Fu
%define upstream_version 0.11

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    GTK2 Forked Ultimate, a powerful layer on top of Gtk2 (forked from ugtk2)
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    http://search.cpan.org/CPAN/authors/id/D/DA/DAMS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-Gtk2

BuildArch: noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
gtk2-fu is a layer on top of perl gtk2, that brings power, simplicity
and speed of development. It brings additional methods to ease the widget
creation among other things. But the most important feature is that it
brings you a lot of derivated methods from existing methods, that does
exactly the same thing, except that ir returns the widget.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%{perl_vendorlib}/*
%{_mandir}/man3/*
