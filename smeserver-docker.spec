%define name smeserver-docker
%define version 0.2
%define release 3
Summary: Contrib to manage basic docker setup
Name: %{name}
Version: %{version}
Release: %{release}
License: GNU GPL version 2
URL: http://www.docker.com/
Group: SMEserver/addon
Source: %{name}-%{version}.tar.gz
# Patch1: smeserver-docker-xxxx.patch


BuildRoot: /var/tmp/%{name}-%{version}
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
Requires:  e-smith-release >= 9.2
Requires:  docker-io >= 1.7.1
AutoReqProv: no

%description
Docker is an open-source project that automates the deployment of applications inside software containers

%changelog
* Thu Dec 20 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-3
- Fix error in spec file

* Thu Dec 20 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-2
- Templating for docker-compose.yml
- docker-update action to expand files - needs actions as well later
- add network and subnet keys
- add masq template fragment to allo wlocal access in bridge mode

* Fri Aug 17 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.2-1
- Add template directory for docker-compose.yml
- You can then add templates from your own contrib

* Sun Apr 08 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-5
- Missed a # in /etc/sysconfig/docker

* Tue Mar 27 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-4
- Missed a # in the spec file

* Thu Mar 15 2018 John Crisp <jcrisp@safeandsoundit.co.uk> 0.1-3
- add rc.7 service links for docker and mongod
- Fix prelink error on docker-compose see https://github.com/docker/compose/issues/
- fix errant semi colon in createlinks
- move demo docker file out of configs so it doesn't overwrite originals

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

# Add configs directory if it doesn't exist
if [[ ! -d /home/e-smith/files/docker/configs ]]; then
mkdir -p /home/e-smith/files/docker/configs;
fi

echo "========================================================================"
echo "see https://wiki.contribs.org/Docker"
echo "Note that docker is not daemonised so config docker status has no effect"
echo "========================================================================"

%postun
