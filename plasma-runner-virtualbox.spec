Summary:        Virtualbox KDE runner
Name:           plasma-runner-virtualbox
Version:        0.3.3
Release:        1
Source:         http://kde-apps.org/CONTENT/content-files/107926-vbox-runner-%{version}.tar.gz
License:        GPLv2+                                         
Group:          Graphical desktop/KDE                          
URL:            https://kde-apps.org/content/show.php/VBox+Runner?content=107926
BuildRequires:  kdelibs4-devel                                     
Requires:	virtualbox
Obsoletes:           virtualbox-kde-runner

%description
Allows you to start your VirtualBox virtual machines from Krunner
(the Alt-F2 thing)

%files
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

