Name:           dqlite
Version:        1.16.4
Release:        0.1%{?dist}
Summary:        Embeddable, replicated and fault tolerant SQL engine

License:        LGPL-3.0-only WITH LGPL-3.0-linking-exception
URL:            https://github.com/canonical/dqlite
Source0:        %{URL}/archive/v%{version}.tar.gz
# https://github.com/canonical/dqlite/issues/574
Patch0:         dqlite-1.16.4-raft-uv-Drop-AI_V4MAPPED-AI_ADDRCONFIG-from-getaddrinfo.patch

BuildRequires:  autoconf libtool
BuildRequires:  gcc
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(sqlite3)

%description
dqlite is a C library that implements an embeddable and replicated SQL database
engine with high-availability and automatic failover.

%package devel
Summary:        Development libraries for dqlite
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development headers and library for dqlite.

%prep
%autosetup -n %{name}-%{version} -p1

%build
autoreconf -i
%configure --disable-static --enable-build-raft=yes
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdqlite.la

%check
%make_build check

%ldconfig_scriptlets

%files
%doc AUTHORS README.md
%license LICENSE
%{_libdir}/libdqlite.so.*

%files devel
%{_libdir}/libdqlite.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h

%changelog
* Mon Mar 25 2024 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.16.4-0.1
- Update to 1.16.4.

* Fri Dec 22 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.16.0-0.2
- Rebuild due to raft ABI change

* Fri Sep 29 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.16.0-0.1
- Update to 1.16.0.

* Sun Jun 18 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.15.1-0.1
- Update to 1.15.1.

* Sat Jan 21 2023 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.14.0-0.1
- Update to 1.14.0.

* Sun Dec 18 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.13.0-0.1
- Update to 1.13.0.

* Sun Dec 04 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.12.0-0.1
- Update to 1.12.0.

* Sat Oct 01 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.11.1-0.2
- Fix build dependencies
- Add patch to fix test issue

* Wed Jul 13 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.11.1-0.1
- Update to 1.11.1.

* Sat Jul 09 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.11.0-0.1
- dqlite: Update to 1.11.0.

* Mon Apr 18 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.10.0-0.1
- Update to 1.10.0.

* Mon Feb 14 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.9.1-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jan 30 2022 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.9.1-0.1
- Update to 1.9.1.

* Mon Aug 23 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.9.0-0.1
- Update to 1.9.0.

* Mon Jun 28 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.8.0-0.1
- Update to 1.8.0.

* Thu May 13 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.7.0-0.1
- Update to 1.7.0

* Wed Apr 28 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.6.0-0.2.20210317gitc0699eb
- Update to git snapshot c0699eb

* Sun Mar 14 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.6.0-0.2.20201229gita89301a
- Skip failing test on Fedora 32

* Sat Mar 13 2021 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.6.0-0.1.20201229gita89301a
- Update to git snapshot a89301a

* Wed Nov 25 2020 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 1.6.0-0.1.20200926git867d7b2
- Initial package.
