Summary:       Langpacks plugin for yum
Name:          yum-langpacks
Version:       0.4.2
Release:       3%{?dist}
License:       GPLv2+
Group:         Development/Tools
Source0:       https://fedorahosted.org/releases/y/u/%{name}/%{name}-%{version}.tar.gz
# upstream commited patches
Patch0:        yum-langpacks-0.4.2-fix-langinfo-command.patch

URL:           https://fedorahosted.org/yum-langpacks/
BuildArch:     noarch
BuildRequires: python-setuptools
BuildRequires: python2-devel
Requires:      yum >= 3.0
Requires:      langtable-python

%description
Yum-langpacks is a plugin for YUM that looks for langpacks for your native
language for packages you install.

%prep
%setup -q
%patch0 -p1

%build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}
gzip yum-langpacks.8
mkdir -p %{buildroot}%{_mandir}/man8
install -p -m 644 yum-langpacks.8.gz %{buildroot}%{_mandir}/man8/yum-langpacks.8.gz

%files
%doc README COPYING
%{python2_sitelib}/*
%{_prefix}/lib/yum-plugins/langpacks.py*
%config(noreplace) %{_sysconfdir}/yum/pluginconf.d/langpacks.conf
%{_mandir}/man8/yum-langpacks.8.gz

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.4.2-3
- Mass rebuild 2013-12-27

* Wed Nov 20 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-2
- Resolves:rh#1029789: yum langinfo only lists langpacks for installed packages

* Tue Oct 08 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.2-1
- Resolves:rh#1013514: Some more optimization for yum langavailable shows nothing

* Mon Sep 30 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-3
- Resolves:rh#1013514: Fixed yum langavailable shows nothing

* Wed Sep 25 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-2
- Resolves:rh#1011674: Fix issue of yum-langpacks commands that slows down yum runs

* Thu Sep 12 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.1-1
- Fix yum langavailable command output (rh#1006695)

* Wed Sep 11 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-3
- Add Requires: langtable-python (rh#1006417)

* Tue Sep 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-2
- use correct macro for python command in %%install
- Add BR: python2-devel

* Tue Sep 10 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.4.0-1
- update to 0.4.0

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 03 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.3.4-1
- update to 0.3.4

* Tue Apr 16 2013 Parag Nemade <pnemade AT redhat DOT com> - 0.3.1-2
- Added langinfo command (rh#952578)

* Fri Mar 29 2013 Jens Petersen <petersen@redhat.com> - 0.3.1-1
- update to 0.3.1
- have to be root also to run langinstall (Parag Nemade, #928833)

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Jens Petersen <petersen@redhat.com> - 0.3.0-4
- update source and project urls
- minor spec cleanup

* Tue Sep 25 2012 Bill Nottingham <notting@redhat.com> - 0.3.0-3
- fix traceback on groupremove (#858175)

* Mon Aug 13 2012 Bill Nottingham <notting@redhat.com> - 0.3.0-2
- fix groupinstall of langonly groups (#840885)
- fix plugin type for use in yumex, elsewhere (#847502)

* Wed Aug 08 2012 Bill Nottingham <notting@redhat.com> - 0.3.0-1
- add langinstall/langremove/langlist commands (#840885)

* Thu Jun 21 2012 Bill Nottingham <notting@redhat.com> - 0.2.5-1
- don't exit on XML errors (#825811, #830739, <zpavlas@redhat.com>)

* Thu Dec 15 2011 Bill Nottingham <notting@redhat.com> - 0.2.4-2
- fix bad interaction with -C (#758574, <zpavlas@redhat.com>)

* Wed Oct 26 2011 Bill Nottingham <notting@redhat.com> - 0.2.4-1
- don't crash when there are no groups (#749108)

* Mon Oct 24 2011 Bill Nottingham <notting@redhat.com> - 0.2.3-1
- use compressed group metadata where possible (#748186)

* Mon Mar 14 2011 Bill Nottingham <notting@redhat.com> - 0.2.2-1
- don't match in-progress updates as removals (#684817)

* Fri Mar 11 2011 Bill Nottingham <notting@redhat.com> - 0.2.1-1
- fix it to work on provides, not just names (#681747)

* Tue Mar 08 2011 Bill Nottingham <notting@redhat.com> - 0.2.0-1
- update to new version that works on metadata (#681747, #682114)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Apr 24 2010 James Antill <james.antill@redhat.com> - 0.1.5-2
- Fix the problems where langpacks could delete the system.
- Resolves: bug#585424
- Register the package name, for yum history etc.

* Thu Mar 11 2010 Jens Petersen <petersen@redhat.com> - 0.1.5-1
- fixes and improvements from James Antill (#571845):
  - Move print's => yum logger uses.
  - Move tsinfo ops to real install/remove ops, so deps will be solved
  - Handles erase properly.
  - Doesn't force upgrade langpacks on upgrades/downgrades/etc.
  - Doesn't try to install multiple versions of langpacks. (#569352)
  - Move from d.has_key(v) to "v in d", as py3 removes the former.

* Tue Dec  8 2009 Jens Petersen <petersen@redhat.com> - 0.1.4-2
- fix source url (#536737)
- drop python requires (#536737)
- drop buildroot and cleaning of buildroot (#536737)
- use global (#536737)

* Mon Nov 16 2009 Jens Petersen <petersen@redhat.com> - 0.1.4-1
- BR python-setuptools (#536737)
- remove shebang from langpacks.py (#536737)

* Wed Nov 11 2009 Jens Petersen <petersen@redhat.com> - 0.1.3-1
- initial package (#433512)
