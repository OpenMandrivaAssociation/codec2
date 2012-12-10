%define	snap r195

%define	major 0
%define libname %mklibname codec2 _%{major}
%define develname %mklibname codec2 -d

Summary:	Low bit rate speech codec
Name:		codec2
Version:	0.1
Release:	0.0.%{snap}.2
License:	LGPL
Group:		Sound
URL:		http://rowetel.com/codec2.html
Source0:	%{name}-%{snap}.tar.gz
Patch0:		codec2-shared.diff
BuildRequires:	libtool

%description
Codec2 is an open source low bit rate speech codec designed for communications
quality speech at around 2400 bit/s. Applications include low bandwidth HF/VHF
digital radio. It fills a gap in open source, free-as-in-speech voice codecs
beneath 5000 bit/s.

%package -n	%{libname}
Summary:	Shared %{name} library
Group:		System/Libraries

%description -n	%{libname}
Codec2 is an open source low bit rate speech codec designed for communications
quality speech at around 2400 bit/s. Applications include low bandwidth HF/VHF
digital radio. It fills a gap in open source, free-as-in-speech voice codecs
beneath 5000 bit/s.

%package -n	%{develname}
Summary:	Development files for the %{name} library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
Codec2 is an open source low bit rate speech codec designed for communications
quality speech at around 2400 bit/s. Applications include low bandwidth HF/VHF
digital radio. It fills a gap in open source, free-as-in-speech voice codecs
beneath 5000 bit/s.

This package contains the development files for codec2.

%prep

%setup -q -n %{name}
%patch0 -p0

%build
%make -C src CFLAGS="%{optflags} -I. -DFLOATING_POINT -DVAR_ARRAYS" LDFLAGS="%{ldflags}" libdir=%{_libdir}

%install
%makeinstall_std -C src \
    bindir=%{_bindir} \
    libdir=%{_libdir} \
    includedir=%{_includedir}

%files
%{_bindir}/*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
%{_libdir}/*.so

