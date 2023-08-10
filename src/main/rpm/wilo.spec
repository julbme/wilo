Name:           ${project.artifactId}
Version:        ${j3.var.rpmVersion}
Release:        ${j3.var.rpmReleaseVersion}
Summary:        ${project.description}
BuildArch:      noarch

License:        MIT
Source0:        ${project.artifactId}-${project.version}.tar.gz

Requires:       jq

%description
${project.description}

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp bin/%{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}

%changelog
* Fri Aug 11 2023 Julien B <julien@julb.me>
- 1.0.3: build a RPM distribution
* Thu Aug 10 2023 Julien B <julien@julb.me>
- 1.0.2: build a Homebrew distribution
* Tue Aug 8 2023 Julien B <julien@julb.me>
- 1.0.1: distribute binary package under SDK well-formed practices.
* Tue Aug 8 2023 Julien B <julien@julb.me>
- 1.0.0: initial version of the tool