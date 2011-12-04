Summary:	NUT (Network UPS Tools) extension for Python
Name:		python-pynut
Version:	1.2
Release:	1
Group:		Development/Python 
License:	GPLv3+
URL:		http://www.lestat.st/informatique/projets/pynut-en
Source0:	http://www.lestat.st/_media/informatique/projets/pynut/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel

%description
PyNUT is an abstraction class written in Python to access NUT (Network UPS
Tools) server and execute commands without needing to know the communication
protocol. 

%prep

%setup -q -n %{name}-%{version}
chmod 644 *

%build

%install
install -d %{buildroot}%{py_puresitedir}
install -m0644 PyNUT.py %{buildroot}%{py_puresitedir}/

%files 
%defattr(-,root,root)
%doc copyright README test_nut.py.gz
%{py_puresitedir}/PyNUT.py
