Summary:	A nice animation wich appears when you mistype the ls command
Summary(pl):	Fajna animacja, która siê pojawia przy b³ednym wpisaniu ls.
Name:		sl
Version:	3.03
Release:	2
License:	GPL
Group:		Console/Amusements
######		Unknown group!
Source0:	http://ftp.debian.org/debian/pool/main/s/sl/%{name}_%{version}.orig.tar.gz
Source1:	%{name}-debian.tar.gz
Patch0:		%{name}-am.patch
Patch1:		%{name}-code.patch
URL:		http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you type sl instead of ls, you will be greeted with a nice and
relaxing animation of a train going by...

%description -l pl
Je¿eli wpiszesz sl, zamiast ls, zostaniesz powitany fajn±
i relaksuj±c± animacja przeje¿dzaj±cego poci±gu...

%prep
%setup -q -n sl-3.03.orig -a1
%patch0 -p1
%patch1 -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{jp/,}man6}

install sl $RPM_BUILD_ROOT/%{_bindir}
install sl-debian/sl.6 $RPM_BUILD_ROOT/%{_mandir}/man6
install sl-debian/sl.6j $RPM_BUILD_ROOT/%{_mandir}/jp/man6/sl.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sl-debian/README
%lang(jp) %doc sl-debian/README.jp
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%lang(jp) %{_mandir}/jp/man6/*
