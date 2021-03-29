#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jaraco.functools
Version  : 3.3.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/fa/cc/e41cd71c277e36f4f2ecd3d550bd27e17677f0601331d54e9e8e4b3ed44d/jaraco.functools-3.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/fa/cc/e41cd71c277e36f4f2ecd3d550bd27e17677f0601331d54e9e8e4b3ed44d/jaraco.functools-3.3.0.tar.gz
Summary  : Functools like those found in stdlib
Group    : Development/Tools
License  : MIT
Requires: jaraco.functools-license = %{version}-%{release}
Requires: jaraco.functools-python = %{version}-%{release}
Requires: jaraco.functools-python3 = %{version}-%{release}
Requires: more-itertools
BuildRequires : buildreq-distutils3
BuildRequires : more-itertools
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : setuptools_scm
BuildRequires : tox
BuildRequires : virtualenv

%description
.. image:: https://img.shields.io/pypi/v/jaraco.functools.svg
:target: `PyPI link`_

%package license
Summary: license components for the jaraco.functools package.
Group: Default

%description license
license components for the jaraco.functools package.


%package python
Summary: python components for the jaraco.functools package.
Group: Default
Requires: jaraco.functools-python3 = %{version}-%{release}

%description python
python components for the jaraco.functools package.


%package python3
Summary: python3 components for the jaraco.functools package.
Group: Default
Requires: python3-core
Provides: pypi(jaraco.functools)
Requires: pypi(more_itertools)

%description python3
python3 components for the jaraco.functools package.


%prep
%setup -q -n jaraco.functools-3.3.0
cd %{_builddir}/jaraco.functools-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1617028457
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/jaraco.functools
cp %{_builddir}/jaraco.functools-3.3.0/LICENSE %{buildroot}/usr/share/package-licenses/jaraco.functools/8e6689d37f82d5617b7f7f7232c94024d41066d1
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/jaraco.functools/8e6689d37f82d5617b7f7f7232c94024d41066d1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
