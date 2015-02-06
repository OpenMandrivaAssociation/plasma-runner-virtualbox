
Summary:        Virtualbox KDE runner
Name:           plasma-runner-virtualbox
Version:        0.2 
Release:        4
Source:         http://kde-apps.org/CONTENT/content-files/107926-vbox-runner-%{version}.tar.gz
License:        GPLv2+                                         
Group:          Graphical desktop/KDE                          
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:            http://kde-apps.org/content/show.php/VBox+Runner?content=107926
BuildRequires:  kdelibs4-devel                                     
Requires:	virtualbox
Obsoletes:           virtualbox-kde-runner

%description
Allows you to start your VirtualBox virtual machines from Krunner
(the Alt-F2 thing)

%files
%defattr(-,root,root)
%doc COPYING
%{_kde_libdir}/kde4/*.so
%{_kde_services}/*
%{_datadir}/pixmaps/vbox-runner/*
#--------------------------------------------------------------------

%prep
%setup -qn vbox-runner-%{version}

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

%clean
rm -rf $RPM_BUILD_ROOT




%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-2mdv2011.0
+ Revision: 614587
- the mass rebuild of 2010.1 packages

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - New name
    - New name

* Sat Feb 20 2010 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0.2-1mdv2010.1
+ Revision: 508842
- import virtualbox-kde-runner

