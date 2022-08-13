Name     : playerctl
Version  : 2.4.1
Release  : 1
URL      : https://github.com/acrisci/playerctl
Source0  : https://github.com/altdesktop/playerctl/archive/refs/tags/v%{version}.tar.gz
Summary  : Command-line MPRIS-compatible Media Player Controller
Group    : Development/Tools
License  : LGPLv3+
BuildRequires : dbus-dev
BuildRequires : buildreq-meson cmake
BuildRequires : glib-dev
BuildRequires : gobject-introspection-dev
BuildRequires : bash-completion-dev

%description
Command-line MPRIS-compatible Media Player Controller.

%package dev
Summary:        Development libraries and header files
Requires:       %{name} = %{version}-%{release}
 
%description dev
Command-line MPRIS-compatible Media Player Controller.

%package lib
Summary:        Libraries and shared code
Requires:       %{name} = %{version}-%{release}
 
%description lib
Libraries and shared code

%prep
%setup -q

%build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FCFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export FFLAGS="$CFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
export CXXFLAGS="$CXXFLAGS -Ofast -fno-lto -falign-functions=32 -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -mno-vzeroupper -mprefer-vector-width=256  "
meson \
    --libdir=lib64 --prefix=/usr \
    -Dbash-completions=true -Dzsh-completions=true -Dgtk-doc=false \
    --buildtype=plain builddir
ninja -v -C builddir

%install
DESTDIR=%{buildroot} ninja -C builddir install
rm -rf %{buildroot}/usr/share/man

%files
%defattr(-,root,root,-)
/usr/bin/playerctl
/usr/bin/playerctld
/usr/share/bash-completion/
/usr/share/dbus-1/services/org.mpris.MediaPlayer2.playerctld.service
/usr/share/zsh

%files lib
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/
/usr/lib64/libplayerctl.so.*

%files dev
%defattr(-,root,root,-)	
/usr/share/gir-1.0/
/usr/include/playerctl/
/usr/lib64/libplayerctl.so
/usr/lib64/pkgconfig/playerctl.pc
/usr/share/abi/libplayerctl.so.2.abi
