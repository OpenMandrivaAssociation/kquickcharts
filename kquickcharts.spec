%define devname %mklibname KF5QuickCharts -d
%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kquickcharts
Version:	5.72.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: A QtQuick module providing high-performance charts.
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5QuickControls2)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: cmake(ECM)
BuildRequires: cmake(Qt5)
# (tpg) kill wrong library
%rename %{_lib}KF5QuickCharts5

%description
The Quick Charts module provides a set of charts that can be used from
QtQuick applications. They are intended to be used for both simple display
of data as well as continuous display of high-volume data (often referred
to as plotters).

The charts use a system called distance fields for their accelerated
rendering, which provides ways of using the GPU for rendering 2D shapes
without loss of quality.

%package -n %{devname}
Summary: Development files for the KDE Frameworks 5 QuickCharts library
Group: Development/KDE and Qt
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files for the KDE Frameworks 5 QuickCharts library.

The Quick Charts module provides a set of charts that can be used from
QtQuick applications. They are intended to be used for both simple display
of data as well as continuous display of high-volume data (often referred
to as plotters).

The charts use a system called distance fields for their accelerated
rendering, which provides ways of using the GPU for rendering 2D shapes
without loss of quality.

%prep
%autosetup -p1
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_libdir}/qt5/qml/org/kde/quickcharts

%files -n %{devname}
%{_libdir}/cmake/KF5*
