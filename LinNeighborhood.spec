Summary:	GUI for a Network Neighborhood in LINUX
Summary(pl):	GUI dla Otoczenia Sieciowego (SMB) w Linuksie
Name:		LinNeighborhood
Version:	0.6.3
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://www.bnro.de/~schmidjo/download/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
URL:		http://www.bnro.de/~schmidjo/
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
Requires:	samba-client >= 2.2.0
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
This application gives you a GUI similar to the Win9x/NT network
neighborhood. It makes you able to browse entire networks and mount
shares.

%description -l pl
Ta aplikacja dostarcza Ci GUI podobnego do Otoczenia Sieciowego w
Win9x/NT. Narzêdzie to pozwala na przegl±danie ca³ych sieci oraz
montowanie udostêpnianych zasobów.

%prep
%setup -q

%build
rm missing
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Network/Misc,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install LinNeighborhood.xpm $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Network/Misc

gzip -9nf AUTHORS BUGS CONFIGURATION NEWS README THANKS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/*
%{_applnkdir}/Network/Misc/*
