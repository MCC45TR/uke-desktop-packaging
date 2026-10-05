%global debug_package %{nil}
%global source_date 20260819
Name: libstdcxx-uke-runtime
Version: 16.2.1
Release: 2.uke1%{?dist}.1
Summary: Native GNU C++ runtime source build for the Uke package selection
License: GPL-3.0-or-later WITH GCC-exception-3.1
URL: https://gcc.gnu.org/onlinedocs/libstdc++/
Source0: gcc-%{version}-%{source_date}.tar.xz
Source1: runtime-smoke.cpp
Source2: fedora-exported-symbols.txt
Source99: gcc-16.2.1-2.fc46.1.src.rpm
Patch4: gcc16-libtool-no-rpath.patch
ExclusiveArch: aarch64
BuildRequires: gcc-c++ = 16.2.1-2.fc46.1
BuildRequires: python3 = 3.15.0~rc2-1.fc46
BuildRequires: make binutils glibc-devel tzdata
%description
Complete reviewed GCC source and build rules for a standalone native libstdc++.
The binary subpackage retains the GNU C++ ABI and excludes optional Python GDB
pretty-printers. No compiler or Python tool is installed on the tablet.
%package -n libstdc++
Summary: GNU Standard C++ Library without optional Python GDB helpers
Provides: senemos-native-runtime(libstdc++) = %{version}-%{release}
Requires: glibc >= 2.10.90-7
Recommends: tzdata >= 2017c
%description -n libstdc++
The native GNU Standard C++ Library, rebuilt from the exact Fedora GCC source.
Optional GDB Python printers are outside this target runtime. The source build
checks the original versioned symbol set and executes a native C++ smoke test.
%prep
%setup -q -n gcc-%{version}-%{source_date}
# The inherited patch changes the shared libtool infrastructure used here.
# Remaining Fedora patches affect compilers, other languages or HTML manuals;
# the complete original source RPM is retained as Source99 for provenance.
%patch -P 4 -p0
%build
mkdir -p senemos-libstdcxx-build
cd senemos-libstdcxx-build
export CC=gcc CXX=g++
export CFLAGS="%{build_cflags}" CXXFLAGS="%{build_cxxflags}" LDFLAGS="%{build_ldflags}"
../libstdc++-v3/configure --prefix=%{_prefix} --libdir=%{_libdir} \
  --build=%{_build} --host=%{_host} --disable-multilib \
  --enable-shared --enable-threads=posix --enable-__cxa_atexit \
  --enable-gnu-unique-object --enable-libstdcxx-backtrace \
  --with-libstdcxx-zoneinfo=%{_datadir}/zoneinfo --disable-libstdcxx-pch
%make_build
%check
cd senemos-libstdcxx-build
nm -D --defined-only src/.libs/libstdc++.so.6.0.36 | awk '{print $3}' | grep '@' | LC_ALL=C sort -u > native-symbols.txt
LC_ALL=C comm -23 %{SOURCE2} native-symbols.txt > missing-symbols.txt
test ! -s missing-symbols.txt || { cat missing-symbols.txt; exit 1; }
g++ -std=c++23 -O2 %{SOURCE1} -L"$PWD/src/.libs" -pthread -o runtime-smoke
LD_LIBRARY_PATH="$PWD/src/.libs" ./runtime-smoke
%install
# Select the runtime library directly from the real source build. Header,
# static-library, documentation and Python debugger targets are not installed.
install -Dm755 senemos-libstdcxx-build/src/.libs/libstdc++.so.6.0.36 %{buildroot}%{_libdir}/libstdc++.so.6.0.36
ln -s libstdc++.so.6.0.36 %{buildroot}%{_libdir}/libstdc++.so.6
if find %{buildroot} -type f \( -name '*.py' -o -name '*.pyc' -o -name '*.pyo' \) -print | grep .; then exit 1; fi
%files -n libstdc++
%license COPYING3 COPYING.RUNTIME
%{_libdir}/libstdc++.so.6
%{_libdir}/libstdc++.so.6.0.36
%changelog
* Mon Oct 05 2026 Senemos Maintainers <75160848+MCC45TR@users.noreply.github.com> - 16.2.1-2.uke1
- Rebuild the native runtime without Python debugger helpers and require ABI/smoke checks.
