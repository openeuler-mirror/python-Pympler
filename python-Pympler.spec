%global _empty_manifest_terminate_build 0
%global         pname Pympler
Name:           python-%{pname}
Version:        0.9
Release:        2
Summary:        A development tool to measure, monitor and analyze the memory behavior of Python objects.
License:        Apache-2.0 and MIT
URL:            https://github.com/pympler/pympler
Source0:        https://files.pythonhosted.org/packages/e8/e2/2f3a086701bb62b1c478a3921836271177838a3c98cdc6b82c3bb36d3854/Pympler-0.9.tar.gz
BuildArch:      noarch
%description
Pympler is a development tool to measure, monitor and analyze the memory
behavior of Python objects in a running Python application.By pympling a Python
application, detailed insight in the size and the lifetime of Python objects can
be obtained. Undesirable or unexpected runtime behavior like memory bloat and
other "pymples" can easily be identified.Pympler integrates three previously
separate projects into a single, comprehensive profiling tool. Asizeof provides
basic size information for one or several Python objects, muppy is used for on-
line monitoring of a Python application and the class tracker provides off-line
analysis of the lifetime of selected Python objects.

%package -n python3-%{pname}
Summary:        A development tool to measure, monitor and analyze the memory behavior of Python objects.
Provides:       python-%{pname}
# Base build requires
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-pip
BuildRequires:  python3-wheel
%description -n python3-%{pname}
Pympler is a development tool to measure, monitor and analyze the memory
behavior of Python objects in a running Python application.By pympling a Python
application, detailed insight in the size and the lifetime of Python objects can
be obtained. Undesirable or unexpected runtime behavior like memory bloat and
other "pymples" can easily be identified.Pympler integrates three previously
separate projects into a single, comprehensive profiling tool. Asizeof provides
basic size information for one or several Python objects, muppy is used for on-
line monitoring of a Python application and the class tracker provides off-line
analysis of the lifetime of selected Python objects.

%package help
Summary:        A development tool to measure, monitor and analyze the memory behavior of Python objects.
Provides:       python3-%{pname}-doc
%description help
Pympler is a development tool to measure, monitor and analyze the memory
behavior of Python objects in a running Python application.By pympling a Python
application, detailed insight in the size and the lifetime of Python objects can
be obtained. Undesirable or unexpected runtime behavior like memory bloat and
other "pymples" can easily be identified.Pympler integrates three previously
separate projects into a single, comprehensive profiling tool. Asizeof provides
basic size information for one or several Python objects, muppy is used for on-
line monitoring of a Python application and the class tracker provides off-line
analysis of the lifetime of selected Python objects.

%prep
%autosetup -n Pympler-0.9 -p1

%build
%py3_build

%install
%py3_install

install -d -m755 %{buildroot}/%{_pkgdocdir}
if [ -d doc ]; then cp -arf doc %{buildroot}/%{_pkgdocdir}; fi
if [ -d docs ]; then cp -arf docs %{buildroot}/%{_pkgdocdir}; fi
if [ -d example ]; then cp -arf example %{buildroot}/%{_pkgdocdir}; fi
if [ -d examples ]; then cp -arf examples %{buildroot}/%{_pkgdocdir}; fi
pushd %{buildroot}
if [ -d usr/lib ]; then
    find usr/lib -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/lib64 ]; then
    find usr/lib64 -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/bin ]; then
    find usr/bin -type f -printf "/%h/%f\n" >> filelist.lst
fi
if [ -d usr/sbin ]; then
    find usr/sbin -type f -printf "/%h/%f\n" >> filelist.lst
fi
touch doclist.lst
if [ -d usr/share/man ]; then
    find usr/share/man -type f -printf "/%h/%f.gz\n" >> doclist.lst
fi
popd
mv %{buildroot}/filelist.lst .
mv %{buildroot}/doclist.lst .

%check
%{__python3} setup.py try

%files -n python3-%{pname} -f filelist.lst

%dir %{python3_sitelib}/*

%files help -f doclist.lst
%{_docdir}/*

%changelog
* Fri Jul 30 2021 chenyanpanHW <chenyanpan@huawei.com> - 0.9-2
- DESC: delete -S git from %autosetup

* Thu Jul 29 2021 OpenStack_SIG <openstack@openeuler.org> - 0.9-1
- Package Spec generate
