Summary:	A nice animation wich appears when you mistype the ls command
Summary(pl.UTF-8):	Fajna animacja, która się pojawia przy błędnym wpisaniu ls
Name:		sl
Version:	5.02
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	https://github.com/mtoyoda/sl/archive/%{version}.tar.gz
# Source0-md5:	5d5fe203eb19598821647ba8db5dde6c
URL:		http://www.tkl.iis.u-tokyo.ac.jp/~toyoda/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
When you type sl instead of ls, you will be greeted with a nice and
relaxing animation of a train going by...

%description -l pl.UTF-8
Jeżeli wpiszesz sl, zamiast ls, zostaniesz powitany fajną i
relaksującą animacja przejeżdżającego pociągu...

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{ja/,}man1}

install sl $RPM_BUILD_ROOT%{_bindir}
install sl.1 $RPM_BUILD_ROOT%{_mandir}/man1
install sl.1.ja $RPM_BUILD_ROOT%{_mandir}/ja/man1/sl.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%lang(ja) %doc README.ja.md
%attr(755,root,root) %{_bindir}/sl
%{_mandir}/man1/sl.1*
%lang(ja) %{_mandir}/ja/man1/sl.1*
