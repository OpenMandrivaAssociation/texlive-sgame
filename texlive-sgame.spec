# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sgame
# catalog-date 2008-12-03 15:15:08 +0100
# catalog-license lppl
# catalog-version 2.14
Name:		texlive-sgame
Version:	2.14
Release:	1
Summary:	LaTeX style for typesetting strategic games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sgame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Formats strategic games. For a 2x2 game, for example, the
input: \begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$
&$3,0$ &$0,9$ \end{game} produces output with (a) boxes around
the payoffs, (b) payoff columns of equal width, and (c) payoffs
vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sgame/sgame.sty
%{_texmfdistdir}/tex/latex/sgame/sgamevar.sty
%doc %{_texmfdistdir}/doc/latex/sgame/README
%doc %{_texmfdistdir}/doc/latex/sgame/sgame.pdf
%doc %{_texmfdistdir}/doc/latex/sgame/sgame.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
