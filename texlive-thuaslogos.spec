%global tl_name thuaslogos
%global tl_revision 51347

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Logos for The Hague University of Applied Sciences (THUAS)
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/thuaslogos
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thuaslogos.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thuaslogos.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains some logos of The Hague University of Applied
Sciences (THUAS). These Logos are available in English and in Dutch.
They are rendered via PGF.

