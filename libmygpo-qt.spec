Summary:	Qt Library that wraps the gpodder.net Web API
Name:		libmygpo-qt
Version:	1.2.0
Release:	1
License:	LGPLv3+
Group:		Development/KDE and Qt
Url:		https://wiki.gpodder.org/wiki/Libmygpo-qt
Source0:   https://github.com/gpodder/libmygpo-qt/archive/%{version}/%{name}-%{version}.tar.gz
#Source0:	http://stefan.derkits.at/files/libmygpo-qt/libmygpo-qt.1.0.8.tar.gz
BuildRequires: make
BuildRequires:	cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
#BuildRequires:	qjson-devel

%description
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

v1.0 wraps nearly every Request from the gpodder.net API except:
-) Simple API Calls Downloading subscription Lists & Uploading
   subscription Lists
-) Retrieving Subscription Changes (you should use "Retrieving Updates
   for a given Device" instead)

#---------------------------------------------------------------------

%define major 1.0
%define libname %mklibname mygpo-qt %{major}

%package -n %{libname}
Summary:	Library for %{name}
Group:		Development/KDE and Qt

%description -n %{libname}
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

v1.0 wraps nearly every Request from the gpodder.net API except:
-) Simple API Calls Downloading subscription Lists & Uploading
   subscription Lists
-) Retrieving Subscription Changes (you should use "Retrieving Updates
   for a given Device" instead)

%files -n %{libname}
%{_libdir}/libmygpo-qt.so.%{major}*
%{_libdir}/libmygpo-qt.so.1

#---------------------------------------------------------------------

%package devel
Summary:	%{name} development files
Group:		Development/KDE and Qt
Requires:	%{libname} = %{version}

%description devel
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

This package contains files need to build applications using libmygpo-qt.

%files devel
%{_libdir}/libmygpo-qt.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/mygpo-qt
%{_libdir}/cmake/mygpo-qt

#---------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake \
         -DMYGPO_BUILD_TESTS=OFF \
         -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%make_build

%install
%make_install -C build
