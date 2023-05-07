%define major	1.0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Name:		codec2
Version:	1.1.0
Release:	1
Summary:	An open source speech codec for 2400 bit/s and below
Group:		Communications/Radio
License:	LGPLv2
Url:		https://github.com/drowe67/codec2
Source0:	https://github.com/drowe67/codec2/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	pkgconfig(samplerate)
BuildRequires:	pkgconfig(speex)
BuildRequires:	pkgconfig(speexdsp)

%description
Codec2 is an open source low bit rate speech codec designed for communications
quality speech between 1200 and 3200 bit/s. Applications include low bandwidth
HF/VHF digital radio and VOIP trunking. Codec 2 operating at 2400 bit/s can
send 26 phone calls using the bandwidth required for one 64 kbit/s uncompressed
phone call. It fills a gap in open source, free-as-in-speech voice codecs
beneath 5000 bit/s.

#----------------------------
%package -n %{libname}
Summary:	Dynamic library files for linking with %{name}

%description -n %{libname}
Dynamic library files for linking with %{name}

#----------------------------
%package -n %{devname}
Summary:	Development files for building packages using %{name}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for building packages using %{name}

%prep
%autosetup -p1

%build
%cmake

%make_build

%install
%make_install -C build

# pkgconfig file
mkdir -p %{buildroot}%{_libdir}/pkgconfig
cat > %{buildroot}%{_libdir}/pkgconfig/%{name}.pc<<EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/%{name}

Name: %{name}
Description: A codec2 codec library
Requires:
Version: %{version}
Libs: -L\${libdir} -l%{name}
Libs.private: -lm
Cflags: -I\${includedir}

EOF

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -r raw wav script %{buildroot}%{_datadir}/%{name}/


%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}

%files -n %{devname}
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/codec2/*

%files
%doc COPYING
#{_bindir}/*
%{_datadir}/%{name}
