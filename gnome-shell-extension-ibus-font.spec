%global uuid          ibus-font-setting@ibus.github.com
%global shortname     ibus-font
%global snapshot_date 20170217

Name:       gnome-shell-extension-%{shortname}
Version:    0.%{snapshot_date}
Release:    1%{?dist}
Summary:    use ibus font setting of ibus setup dialog to enhance the user experience

License:    GPLv3+
URL:        https://extensions.gnome.org/extension/1121/ibus-font-setting/
Source0:    https://pwu.fedorapeople.org/ibus/ibus-font-setting/%{name}-%{snapshot_date}.tar.gz
BuildArch:  noarch

Requires:   gnome-shell
Requires:   ibus

%description
use ibus font setting of ibus setup dialog to enhance the user experience

%prep
%setup -q -c

%build
# None

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
install -Dp -m 0644 {extension.js,metadata.json,prefs.js,stylesheet.css} \
  %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}/

%files
%license COPYING
%{_datadir}/gnome-shell/extensions/%{uuid}/


%changelog

* Fri Feb 17 2017 Kermit Wang <kermitwang@163.com> - 0.20170217-1
- Initialize package for Fedora.
