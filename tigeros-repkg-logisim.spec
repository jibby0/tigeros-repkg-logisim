Name:      tigeros-repkg-logisim
Version:   2.3.1
Release:   1%{?dist}
Summary:   An educational tool for designing and simulating digital logic circuits

License:   GPLv2
URL:       http://www.cburch.com/logisim/

%undefine _disable_source_fetch
Source0: https://sourceforge.net/projects/circuit/files/2.3.x/%{version}/logisim-%{version}.jar/download
%define SHA256SUM0 c0e5fc5f664ea8f9a19854bf5457c2230338699172dd5ca2639ceb1531a59c76
Source1: logisim
Source2: logisim.desktop
Source3: https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logisim-icon.svg/240px-Logisim-icon.svg.png
%define SHA256SUM3 3693f7c9e885a93eea7310cc993cc7f516dc8eee46543a538c30587ec18df0ca

BuildArch: noarch
Requires:  java-1.8.0-openjdk

%description
Logisim is an educational tool for designing and simulating digital
logic circuits. With its simple toolbar interface and simulation of
circuits as you build them, it is simple enough to facilitate
learning the most basic concepts related to logic circuits. With the
capacity to build larger circuits from smaller subcircuits, and to
draw bundles of wires with a single mouse drag, Logisim can be used
(and is used) to design and simulate entire CPUs for educational
purposes.

%prep
echo "%SHA256SUM0 %SOURCE0" | sha256sum -c -
echo "%SHA256SUM3 %SOURCE3" | sha256sum -c -

%install
# Install the jar to /usr/share/java
%{__mkdir_p} %{buildroot}%{_datadir}/java/
install -p -m 755 %{SOURCE0} %{buildroot}%{_datadir}/java/logisim-%{version}.jar

# Install the wrapper script
%{__mkdir_p} %{buildroot}%{_prefix}/local/bin/
install -p -m 755 %{SOURCE1} %{buildroot}%{_prefix}/local/bin/

# Install the .desktop file
%{__mkdir_p} %{buildroot}%{_prefix}/local/share/applications/
install -p -m 644 %{SOURCE2} %{buildroot}%{_prefix}/local/share/applications/

# Install the icon
%{__mkdir_p} %{buildroot}%{_prefix}/local/share/icons/
install -p -m 644 %{SOURCE3} %{buildroot}%{_prefix}/local/share/icons/logisim.jpg

%files
%{_prefix}/local/bin/logisim
%{_prefix}/local/share/applications/logisim.desktop
%{_prefix}/local/share/icons/logisim.jpg
%{_prefix}/share/java/logisim-%{version}.jar

%changelog
* Mon May 21 2018 Josh Bicking <jhb2345@rit.edu> - 2.3.1-1
- Initial revision
- Update specfile to match TigerOS RPM layout
