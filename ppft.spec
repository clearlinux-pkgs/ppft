#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ppft
Version  : 1.7.6.6
Release  : 10
URL      : https://github.com/uqfoundation/ppft/releases/download/ppft-1.7.6.6/ppft-1.7.6.6.tar.gz
Source0  : https://github.com/uqfoundation/ppft/releases/download/ppft-1.7.6.6/ppft-1.7.6.6.tar.gz
Summary  : distributed and parallel python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: ppft-bin = %{version}-%{release}
Requires: ppft-license = %{version}-%{release}
Requires: ppft-python = %{version}-%{release}
Requires: ppft-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi(setuptools)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
ppft
====
distributed and parallel python
About Ppft
----------
``ppft`` is a friendly fork of Parallel Python (``pp``). ``ppft`` extends Parallel Python to provide packaging and distribution with ``pip`` and ``setuptools``, support for python 3, and enhanced serialization using ``dill.source``. ``ppft`` uses Parallel Python to provide mechanisms for the parallel execution of python code on SMP (systems with multiple processors or cores) and clusters (computers connected via network).

%package bin
Summary: bin components for the ppft package.
Group: Binaries
Requires: ppft-license = %{version}-%{release}

%description bin
bin components for the ppft package.


%package license
Summary: license components for the ppft package.
Group: Default

%description license
license components for the ppft package.


%package python
Summary: python components for the ppft package.
Group: Default
Requires: ppft-python3 = %{version}-%{release}

%description python
python components for the ppft package.


%package python3
Summary: python3 components for the ppft package.
Group: Default
Requires: python3-core
Provides: pypi(ppft)

%description python3
python3 components for the ppft package.


%prep
%setup -q -n ppft-1.7.6.6
cd %{_builddir}/ppft-1.7.6.6
pushd ..
cp -a ppft-1.7.6.6 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666629732
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ppft
cp %{_builddir}/ppft-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ppft/7dd3b63ab14ec21f8db6b624104d1677a7cffaed || :
cp %{_builddir}/ppft-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/ppft/b3202f384769f215a28d14e52020c96201722bda || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ppserver

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ppft/7dd3b63ab14ec21f8db6b624104d1677a7cffaed
/usr/share/package-licenses/ppft/b3202f384769f215a28d14e52020c96201722bda

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
