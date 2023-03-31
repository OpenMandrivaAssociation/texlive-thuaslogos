Name:		texlive-thuaslogos
Version:	51347
Release:	2
Summary:	Logos for The Hague University of Applied Sciences (THUAS)
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/thuaslogos
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuaslogos.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/thuaslogos.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains some logos of The Hague University of
Applied Sciences (THUAS). These Logos are available in English
and in Dutch. They are rendered via PGF.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/thuaslogos
%doc %{_texmfdistdir}/doc/latex/thuaslogos

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
