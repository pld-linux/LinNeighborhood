Summary:	GUI for a Network Neighborhood in LINUX
Summary(pl):	GUI dla S�siedztwa Sieciowego (SMB) w Linuksie
Name:		LinNeighborhood
Version:	0.6.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.bnro.de/~schmidjo/download/%{name}-%{version}.tar.gz
Patch0:		http://www.bnro.de/~schmidjo/download/patch-0.6.1-es-pt_BR.gz
URL:		http://www.bnro.de/~schmidjo/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
Requires:	samba
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This application gives you a GUI similar to the Win9x/NT
network neighborhood. It makes you able to browse entire
networks and mount shares.

%description -l pl
Ta aplikacja dostarcza Ci GUI podobnego do Otoczenia Sieciowego
w Win9x/NT. Narz�dzie to pozwala na przegl�danie ca�ych sieci
oraz montowanie udost�pnianych zasob�w.

%prep
%setup -q
%patch0 -p1

%build
gettextize --copy --force
autoconf
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Applications,%{_datadir}/pixmaps}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install LinNeighborhood.xpm	$RPM_BUILD_ROOT%{_datadir}/pixmaps
install linneighborhood.desktop $RPM_BUILD_ROOT%{_applnkdir}/Applications

gzip -9nf AUTHORS BUGS CONFIGURATION NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/pixmaps/LinNeighborhood.xpm
%{_applnkdir}/Applications/linneighborhood.desktop
