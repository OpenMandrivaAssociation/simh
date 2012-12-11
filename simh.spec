# Based on spec from Fedora

Name:		simh
Version:	3.8.1
Release:	%mkrel 1
Summary:	A highly portable, multi-system emulator
Group:		Emulators
License:	MIT and GPLv1+
URL:		http://simh.trailing-edge.com/
Source0:	simh-%{version}-noroms.tar.gz
# we use this to remove the roms binary and patented code before shipping it.
# Download the upstream tarball and invoke this script while in the
# tarball's directory: ./simh-generate-tarball.sh 3.8.1
Source1:	simh-generate-tarball.sh
Patch0:		simh-3.8.1-makefile.patch
Patch1:		simh-3.8.1-altair-segfault.patch
Patch2:		simh-3.8.1-fmt.patch
BuildRequires:	pcap-devel
BuildRequires:	dos2unix

%description
SIMH is a historical computer simulation system. It consists of simulators
for many different computers, all written around a common user
interface package and set of supporting libraries.
SIMH can be used to simulate any computer system for which sufficient detail
is available, but the focus to date has been on simulating computer systems
of historic interest.

SIMH implements simulators for:

* Data General Nova, Eclipse
* Digital Equipment Corporation PDP-1, PDP-4, PDP-7, PDP-8, PDP-9, PDP-10,
  PDP-11, PDP-15, VAX
* GRI Corporation GRI-909, GRI-99
* IBM 1401, 1620, 7090/7094, System 3
* Interdata (Perkin-Elmer) 16b and 32b systems
* Hewlett-Packard 2114, 2115, 2116, 2100, 21MX, 1000
* Honeywell H316/H516
* MITS Altair 8800, with both 8080 and Z80
* Royal-Mcbee LGP-30, LGP-21
* Scientific Data Systems SDS 940

%prep
%setup -q
dos2unix makefile
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%__mkdir_p BIN
export CFLAGS="%{optflags}"
%make USE_NETWORK=1


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
for i in `ls BIN/`; do
	%__install -p -m 755 BIN/$i %{buildroot}%{_bindir}/simh-$i
done
for i in `find -iname "*.txt"`; do dos2unix -k $i; done

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%doc ALTAIR/altair.txt NOVA/eclipse.txt 0readme_38.txt 0readme_ethernet.txt
%doc HP2100/hp2100_diag.txt I7094/i7094_bug_history.txt Interdata/id_diag.txt
%doc PDP1/pdp1_diag.txt PDP10/pdp10_bug_history.txt PDP18B/pdp18b_diag.txt
%doc S3/haltguide.txt S3/readme_s3.txt S3/system3.txt SDS/sds_diag.txt
%doc VAX/vax780_bug_history.txt



%changelog
* Wed Feb 15 2012 Andrey Bondrov <abondrov@mandriva.org> 3.8.1-1mdv2011.0
+ Revision: 774411
- imported package simh

