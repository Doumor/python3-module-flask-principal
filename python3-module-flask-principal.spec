%define pypi_name flask-principal

%def_without check

Name:    python3-module-%pypi_name
Version: 0.4.0
Release: alt1

Summary: Identity management for Flask applications
License: MIT
Group:   Development/Python3
URL:     https://github.com/mattupstate/flask-principal

Packager: Danilkin Danila <danild@altlinux.org>

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%if_with check
BuildRequires: python3-module-pytest
%endif

BuildArch: noarch

Source: %name-%version.tar

%description
Flask-Principal provides a very loose framework to tie in authentication and user information providers, often located in different parts of a webapplication.

%prep
%setup

%build
%pyproject_build

%install
%pyproject_install

%check
%pyproject_run_pytest

%files
%doc README.rst CHANGES LICENSE
%python3_sitelibdir/flask_principal.py
%python3_sitelibdir/Flask_Principal-%version.dist-info/


%changelog
* Wed Oct 24 2023 Danilkin Danila <danild@altlinux.org> 0.4.0-alt1
- Initial build for Sisyphus
