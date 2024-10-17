Summary:	NUT (Network UPS Tools) extension for Python
Name:		python-pynut
Version:	1.11.2
Release:	1
Group:		Development/Python 
License:	GPLv3+
URL:		https://www.lestat.st/informatique/projets/pynut-en
Source0:	https://files.pythonhosted.org/packages/source/p/pynut/pynut-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	python%{pyver}dist(setuptools)

%description
PyNUT is an abstraction class written in Python to access NUT (Network UPS
Tools) server and execute commands without needing to know the communication
protocol. 

%prep
%autosetup -p1 -n pynut-%{version}
find . -type d |xargs chmod 0755
find . -type f |xargs chmod 0644

%build
%py_build

%install
%py_install

%files 
%defattr(-,root,root)
%{py_puresitedir}/pynut*.egg-info
%{py_puresitedir}/pyNut
