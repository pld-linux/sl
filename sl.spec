Summary:	A nice animation wich appears when you mistype the ls command
Summary(pl):	Fajna animacja, która siê pojawia przy b³ednym wpisaniu ls.
Name:		sl
Version:	3.03
Release:	1
License:	GPL
Group:		Console/Amusements
Source0:	http://ftp.debian.org/debian/pool/main/s/sl/sl_%{version}.orig.tar.gz
Patch0:		sl-am.patch
Patch1:		sl-code.patch
#URL:		
BuildRequires:	ncurses-devel
Requires:	ncurses

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr
%define		_mandir		%{_prefix}/man

%description
When you type sl instead of ls, you will be greeted with a nice and relaxing 
animation of a train going by...

%description -l pl
Je¿eli wpiszesz sl, zamiast ls, zostaniesz powitany fajn± i relaksuj±c± animacja przeje¿dzaj±cego poci±gu...

%prep
%setup -q -n sl-3.03.orig
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/man
install -d $RPM_BUILD_ROOT/usr/man/man1
install -p sl $RPM_BUILD_ROOT/%{_prefix}/bin
install -p sl.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
