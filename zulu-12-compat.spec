# Copyright: Nico Kadel-Garcia <nkadel@gmail.com>

Summary: RPM plugin to allow zulu to replace openjdk
Version: 12.2.3
Name: zulu112-compat
Release: 0%{?dist}
License: GPLv2 with exceptions
Group: Development/Tools
URL: http://www.azul.com

Packager: Nico Kadel-Garcia <nkadel@gmail.com>

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: zulu-12 >= %{version}
Provides: 1:java-headless = 1:%{version}
Provides: 1:java-devel = 1:%{version}
Conflicts: java*openjdk*
Conflicts: jdk*

%description
%{name} provides the dependency needed for Java dependent components
to operate with the Zulu %{version} JDK.

%prep
#%setup

%build
true

%install
true

%clean
%{__rm} -rf %{buildroot}

%files

%changelog
* Thu May 23 2019 Nico Kadel-Garcia <nkadel@gmail.com> - 1.12.0-0
- IOnitial setup
