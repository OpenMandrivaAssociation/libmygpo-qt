Summary: Qt Library that wraps the gpodder.net Web API
Name: libmygpo-qt
Version: 1.0.5
Release: 1
Source0: http://stefan.derkits.at/files/%{name}/%{name}.%{version}.tar.gz
Patch0:	       libmygpo-qt-1.0.5-LIB_SUFFIX.patch
License: LGPLv3+
Group: Development/KDE and Qt
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Url: http://wiki.gpodder.org/wiki/Libmygpo-qt
BuildRequires: cmake
BuildRequires: qt4-devel
BuildRequires: qjson-devel

%description
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

v1.0 wraps nearly every Request from the gpodder.net API except:
-) Simple API Calls Downloading subscription Lists & Uploading
   subscription Lists
-) Retrieving Subscription Changes (you should use "Retrieving Updates
   for a given Device" instead)

%define major 1.0
%define libname %mklibname mygpo-qt %major

%package -n %libname
Summary: Library for %{name}
Group: Development/KDE and Qt

%description -n %libname
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

v1.0 wraps nearly every Request from the gpodder.net API except:
-) Simple API Calls Downloading subscription Lists & Uploading
   subscription Lists
-) Retrieving Subscription Changes (you should use "Retrieving Updates
   for a given Device" instead)

%package devel
Summary: %{name} development files
Group: Development/KDE and Qt
Requires: %libname = %version

%description devel
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

This package contains files need to build applications using libmygpo-qt.

%prep
%setup -qn %name.%version
%apply_patches

%build
%cmake -DMYGPO_BUILD_TESTS=OFF
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf %{buildroot}

%files -n %libname
%defattr(-,root,root)
%_libdir/libmygpo-qt.so.%{major}*
%_libdir/libmygpo-qt.so.1

%files devel
%defattr(-,root,root)
%_libdir/libmygpo-qt.so
%_libdir/pkgconfig/*.pc
%_includedir/mygpo-qt
%_libdir/cmake/mygpo-qt


%changelog
* Fri Aug 17 2012 Crispin Boylan <crisb@mandriva.org> 1.0.5-1
+ Revision: 815202
- New release

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2
+ Revision: 662385
- mass rebuild

* Sun Mar 20 2011 Funda Wang <fwang@mandriva.org> 1.0.1-1
+ Revision: 647087
- import libmygpo-qt

