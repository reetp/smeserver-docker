%define name smeserver-docker
%define version 0.1
%define release 2
Summary: Contrib to manage basic docker setup
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://www.docker.com/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
# Patch1: smeserver-docker-xxxx.patch


BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.2
Requires:  mod_proxy_wstunnel >= 0.1
Requires:  docker-io >= 1.7.1
AutoReqProv: no

%description
Docker is an open-source project that automates the deployment of applications inside software containers

%changelog

* Sun Mar 11 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-2
- update spec file to set props on docker-compose
- mover docker-compose to /usr/bin

* Sun Mar 4 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-1
- initial release
- basic file layout
- removed httpd templates - need to create your own

%prep
%setup

# %patch1 -p1

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
--file /usr/bin/docker-compose 'attr(4750,root,root)' \
> %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist


%clean
cd ..
rm -rf %{name}-%{version}

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%pre
%preun
%post

# Included sample compose file
#if [[ ! -d /home/e-smith/files/docker ]]; then
#mkdir -p /home/e-smith/files/docker;
#mkdir -p /home/e-smith/files/docker/configs;
#fi


#/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
#/sbin/e-smith/expand-template /etc/inittab
#/sbin/init q


echo "see https://wiki.contribs.org/Docker"

%postun
#/sbin/e-smith/expand-template /etc/rc.d/init.d/masq
#/sbin/e-smith/expand-template /etc/inittab
#/sbin/init q
