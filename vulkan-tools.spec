%define uname Vulkan-Tools

Name:		vulkan-tools
Version:	1.3.275
Release:	1
Summary:	Vulkan utilities and tools
Group:		Development/Tools
License:	ASL 2.0
URL:		https://github.com/KhronosGroup/Vulkan-Tools
Source0:	https://github.com/KhronosGroup/Vulkan-Tools/archive/v%{version}/%{uname}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	glslang
BuildRequires:	pkgconfig(vulkan)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-cursor)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-server)
BuildRequires:	pkgconfig(wayland-egl)
BuildRequires:	pkgconfig(wayland-eglstream)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(python)

%description
This project provides Khronos official Vulkan Tools and Utilities for
Windows, Linux, Android, and MacOS.

%prep
%autosetup -p1 -n %{uname}-%{version}

%build
%cmake \
    -DVULKAN_HEADERS_INSTALL_DIR=%{_prefix} \
    -DGLSLANG_INSTALL_DIR=%{_bindir}

%make_build

%install
%make_install -C build

%files
%doc README.md CONTRIBUTING.md
%license LICENSE.txt
%{_bindir}/*
