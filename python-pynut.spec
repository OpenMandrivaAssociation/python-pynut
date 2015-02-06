Summary:	NUT (Network UPS Tools) extension for Python
Name:		python-pynut
Version:	1.2
Release:	2
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


%changelog
* Sun Dec 04 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.2-1
+ Revision: 737691
- version update 1.2

* Thu Nov 19 2009 Funda Wang <fwang@mandriva.org> 1.1-3mdv2011.0
+ Revision: 467410
- really use noarch dir
- really use noarch dirs

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-2mdv2010.0
+ Revision: 442444
- rebuild

* Wed Mar 11 2009 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdv2009.1
+ Revision: 353747
- 1.1

* Fri Oct 10 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2009.1
+ Revision: 291400
- try to fix build
- import python-pynut

