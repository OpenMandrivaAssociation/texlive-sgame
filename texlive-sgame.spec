Name:		texlive-sgame
Version:	30959
Release:	2
Summary:	LaTeX style for typesetting strategic games
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sgame
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Formats strategic games. For a 2x2 game, for example, the
input: \begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$
&$3,0$ &$0,9$ \end{game} produces output with (a) boxes around
the payoffs, (b) payoff columns of equal width, and (c) payoffs
vertically centered within the boxes. Note that the game
environment will not work in the argument of another command.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sgame/sgame.sty
%{_texmfdistdir}/tex/latex/sgame/sgamevar.sty
%doc %{_texmfdistdir}/doc/latex/sgame/README
%doc %{_texmfdistdir}/doc/latex/sgame/sgame.pdf
%doc %{_texmfdistdir}/doc/latex/sgame/sgame.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
