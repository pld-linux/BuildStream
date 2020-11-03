Summary:	Framework for modelling build pipelines in YAML
Summary(pl.UTF-8):	Szkielet do modelowania potoków budowania w YAML-u
Name:		BuildStream
Version:	1.6.1
Release:	1
License:	LGPL v2+
Group:		Development/Tools
Source0:	http://ftp.gnome.org/pub/GNOME/sources/BuildStream/1.6/%{name}-%{version}.tar.xz
# Source0-md5:	7afab1908e815ebbd7e4ef1404bf2818
URL:		https://wiki.gnome.org/Projects/BuildStream
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-pytest-runner
BuildRequires:	python3-setuptools
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BuildStream is a Free Software tool for building/integrating software
stacks. It takes inspiration, lessons and use-cases from various
projects including OBS, Reproducible Builds, Yocto, Baserock,
Buildroot, Aboriginal, GNOME Continuous, JHBuild, Flatpak Builder and
Android repo.

%description -l pl.UTF-8
BuildStream to wolnodostępne narzędzie do budowania/integrowania
stosów programowych. Inspiracje, doświadczenia i przypadki użycia
czerpie z różnych projektów, m.in. OBS, Reproducible Builds, Yocto,
Baserock, Buildroot, Aboriginal, GNOME Continuous, JHBuild, Flatpak
Builder oraz repozytorium Androida.

%package -n bash-completion-%{name}
Summary:	Bash completion for bst commands
Summary(pl.UTF-8):	Bashowe uzupełnianie parametrów poleceń bst
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-%{name}
Bash completion for bst commands.

%description -n bash-completion-%{name} -l pl.UTF-8
Bashowe uzupełnianie parametrów poleceń bst.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MAINTAINERS NEWS README.rst
%attr(755,root,root) %{_bindir}/bst
%attr(755,root,root) %{_bindir}/bst-artifact-server
%{py3_sitescriptdir}/buildstream
%{py3_sitescriptdir}/BuildStream-%{version}-py*.egg-info
%{_mandir}/man1/bst.1*
%{_mandir}/man1/bst-*.1*

%files -n bash-completion-%{name}
%defattr(644,root,root,755)
%{bash_compdir}/bst
