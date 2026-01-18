%define major 1.2
%define libname %mklibname mygpo-qt6
%define devname %mklibname -d mygpo-qt6

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
%{_libdir}/libmygpo-qt6.so.%{major}*
%{_libdir}/libmygpo-qt6.so.1

#---------------------------------------------------------------------

%package -n %{devname}
Summary:	%{name} development files
Group:		Development/KDE and Qt
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
libmygpo-qt is a Qt Library that wraps the gpodder.net Web API.

This package contains files need to build applications using libmygpo-qt.


%files -n %{devname}
%{_libdir}/libmygpo-qt6.so
%{_libdir}/pkgconfig/libmygpo-qt6.pc
%{_includedir}/mygpo-qt6/
%{_libdir}/cmake/mygpo-qt6/

#---------------------------------------------------------------------

%prep
%autosetup -n %{name}-%{version} -p1

%build
%cmake \
         -DMYGPO_BUILD_TESTS=OFF \
         -DBUILD_WITH_QT6:BOOL=TRUE \
         -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON
%make_build

%install
%make_install -C build
