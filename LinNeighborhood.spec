Summary:	GUI for a Network Neighborhood in LINUX
Summary(pl.UTF-8):	GUI dla Otoczenia Sieciowego (SMB) w Linuksie
Summary(pt_BR.UTF-8):	Interface gráfica para a vizinhança da rede
Name:		LinNeighborhood
Version:	0.6.5
Release:	5
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://www.bnro.de/~schmidjo/download/%{name}-%{version}.tar.gz
# Source0-md5:	5e50c9cef403164aca22be9ade0a7dbf
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-po.patch
#bugfix for samba 3 mount problem ('can't resolve address'):
# http://www.bnro.de/~schmidjo/download/LinNeighborhood-0.6.5-samba3.patc
Patch1:		%{name}-%{version}-samba3.patch
URL:		http://www.bnro.de/~schmidjo/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
Requires:	samba-client
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This application gives you a GUI similar to the Win9x/NT network
neighborhood. It makes you able to browse entire networks and mount
shares.

%description -l pl.UTF-8
Ta aplikacja dostarcza Ci GUI podobnego do Otoczenia Sieciowego w
Win9x/NT. Narzędzie to pozwala na przeglądanie całych sieci oraz
montowanie udostępnianych zasobów.

%description -l pt_BR.UTF-8
Esta aplicação fornece uma interface gráfica similar a vizinhança da rede
no Win9x/NT (c). Permite a navegação em redes inteiras e montar volumes
compartilhados.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS CONFIGURATION README THANKS TODO ChangeLog
%attr(755,root,root) %{_bindir}/%{name}
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
