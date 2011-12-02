Name:           cjet
Version:        0.8.9
Release:        9.1%{?dist}
Summary:        Converts PCL data to Canon CaPSL III printer language

Group:          System Environment/Libraries
License:        GPLv2+
URL:            ftp://sunsite.unc.edu/pub/Linux/system/printing/cjet089.lsm
Source0:        ftp://sunsite.unc.edu/pub/Linux/system/printing/cjet089.tgz
Patch0:         cjet-0.8.9-clean-build.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This is a filter to convert PCL data such as produced by ghostscript to
the printer language of Canon CaPSL III printers.  It is meant to be used
by the PostScript Description files of the drivers from the foomatic package.

%prep
%setup -q -n cjet089
%patch0 -p1

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT/%{_bindir}
%{__install} cjet $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/cjet
%doc ChangeLog README COPYING TODO

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.8.9-9.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Sep 21 2008 Ville Skyttä <ville.skytta at iki.fi> - 0.8.9-7
- Fix Patch0:/%%patch mismatch.

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.8.9-6
- Autorebuild for GCC 4.3

* Sun Aug 12 2007 Florian La Roche <laroche@redhat.com> 0.8.9-5
- move changelog to utf-8 (#251833)

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.8.9-4
- Fix the compiler flags use for real (#249974)

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.8.9-3
- Modify the License tag in accordance with the new guidelines

* Fri Aug 3 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.8.9-2
- Use compiler flags, thanks to Ville Skyttä (#249974)

* Thu Jun 7 2007 Lubomir Kundrak <lkundrak@redhat.com> 0.8.9-1
- Initial package
