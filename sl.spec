Summary:	A nice animation wich appears when you mistype the ls command
Summary(pl.UTF-8):   Fajna animacja, która się pojawia przy błędnym wpisaniu ls
Name:		sl
Version:	3.03
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/%{name}/%{name}.tar
# Source0-md5:	cc06b159f78f86bfd2d4e0e16330fbae
Source1:	%{name}-debian.tar.gz
# Source1-md5:	a13934db014b77267f1a7109588d4255
Patch0:		%{name}-am.patch
Patch1:		%{name}-code.patch
URL:		http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you type sl instead of ls, you will be greeted with a nice and
relaxing animation of a train going by...

%description -l pl.UTF-8
Jeżeli wpiszesz sl, zamiast ls, zostaniesz powitany fajną
i relaksującą animacja przejeżdżającego pociągu...

%prep
%setup -q -n %{name} -a1
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{ja/,}man6}

install sl $RPM_BUILD_ROOT%{_bindir}
install sl-debian/sl.6 $RPM_BUILD_ROOT%{_mandir}/man6
install sl-debian/sl.6j $RPM_BUILD_ROOT%{_mandir}/ja/man6/sl.6

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc sl-debian/README
%lang(ja) %doc sl-debian/README.jp
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%lang(ja) %{_mandir}/ja/man6/*
