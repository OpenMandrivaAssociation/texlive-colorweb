%global tl_name colorweb
%global tl_revision 31490

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Extend the color package colour space
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/colorweb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package makes the 216 "web-safe colours" available to the standard
color package.

