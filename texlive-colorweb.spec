Name:		texlive-colorweb
Version:	31490
Release:	1
Summary:	Extend the color package colour space
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/colorweb
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/colorweb.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package makes the 216 "web-safe colours" available to the
standard color package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/colorweb/colorweb.sty
%doc %{_texmfdistdir}/doc/latex/colorweb/README
%doc %{_texmfdistdir}/doc/latex/colorweb/colorweb.pdf
%doc %{_texmfdistdir}/doc/latex/colorweb/colorwebfull.pdf
%doc %{_texmfdistdir}/doc/latex/colorweb/colorwebuser.pdf
%doc %{_texmfdistdir}/doc/latex/colorweb/descript.ion
#- source
%doc %{_texmfdistdir}/source/latex/colorweb/colorweb.dtx
%doc %{_texmfdistdir}/source/latex/colorweb/colorweb.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
