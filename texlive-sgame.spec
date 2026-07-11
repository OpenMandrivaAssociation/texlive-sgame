%global tl_name sgame
%global tl_revision 30959

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.15
Release:	%{tl_revision}.1
Summary:	LaTeX style for typesetting strategic games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sgame
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sgame.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Formats strategic games. For a 2x2 game, for example, the input:
\begin{game}{2}{2} &$L$ &$M$\\ $T$ &$2,2$ &$2,0$\\ $B$ &$3,0$ &$0,9$
\end{game} produces output with (a) boxes around the payoffs, (b) payoff
columns of equal width, and (c) payoffs vertically centered within the
boxes. Note that the game environment will not work in the argument of
another command.

