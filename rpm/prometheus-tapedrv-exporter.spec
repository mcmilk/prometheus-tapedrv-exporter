Summary: Tapedrive statistics exporter for Prometheus
Name: prometheus-tapedrv-exporter
Version: 0.1
Release: 1
License: GPL
Group: DESY
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: node_exporter

Source0: usr/sbin/tapedrv-exporter-daemon
Source1: usr/lib/systemd/system/tapedrv-exporter.service
Packager: Tino Reichardt <tino.reichardt@desy.de>

%description
Tapedrive statistics exporter for Prometheus

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{utilsdir}

install -D -m 755 %{SOURCE0} %{buildroot}/usr/sbin/tapedrv-exporter-daemon
install -D -m 644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/tapedrv-exporter.service

%post
if [ $1 -eq 1 ] ; then
	# Initial installation
	systemctl preset tapedrv-exporter.service >/dev/null 2>&1 || :
	systemctl start tapedrv-exporter.service >/dev/null 2>&1 || :
fi

%preun
if [ $1 -eq 0 ] ; then
	# Package removal, not upgrade
	systemctl disable tapedrv-exporter.service > /dev/null 2>&1 || :
	systemctl stop tapedrv-exporter.service > /dev/null 2>&1 || :
	rm -f /var/lib/prometheus/node_exporter/tape_status.prom
fi

%postun
systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
	# Package upgrade, not uninstall
	systemctl try-restart tapedrv-exporter.service >/dev/null 2>&1 || :
fi

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/sbin/*
%{_unitdir}/*

%changelog
* Fri Aug 29 2025 Tino Reichardt <tino.reichardt@desy.de> - 0.1
- initial version
