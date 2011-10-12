%% ECU Thesis style.  Written 2004 by Evin Robertson.
%%
%% Normally LaTeX would nicely typeset your papers for you.
%% This class uses ECU's requirements instead.
%%
%% See http://www.ecu.edu/gradschool/thes_dis/manual.html
%%
%% Plus: undocumented additional requirements:
%%   * everything should use the same size font (no large headings, etc)
%%   * top-level headings should be uppercase, at the top of the page,
%%     and centered
%%   * table of contents should have dots going across for all parts
%%   * should use APA-like bibliography style
%%
%% Much of the signature page stuff is based on the Duke thesis style class
%% Other parts were modified from their versions in the report class
%%
%% Depends on the following packages:
%%  report class
%%  vmargin
%%  setspace
%%  fancyhdr


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ecuthesis}[2004/02/04 ECU Thesis Style]

% Base on report class.
\ProcessOptions
\LoadClass[letterpaper,onecolumn,12pt]{report}
\pagestyle{empty}

\RequirePackage{calc}

%% Margins:
%% Left: 1.5in; Top: 1.5in; Right: 1in; Bottom: 1in
%% The top margin is 1.5 in, But we use 40pts for the page numbering
%% and spacing, so use 1.5 * 72 - 15 - 25 = 68 (a little less than an inch)
\RequirePackage{vmargin}
\setpapersize{USletter}
\setmarginsrb{1.5in}{68pt}{1in}{1in}{15pt}{25pt}{0pt}{0pt}

%% Double Spacing
\RequirePackage{setspace}

%% Single spacing in tables
\renewenvironment{quote}
  { \begin{singlespace} \list{}{\rightmargin\leftmargin} \item\relax}
  { \endlist \end{singlespace} }


%% Single spacing in lists
\let\old@itemize\itemize
\let\endold@itemize\enditemize
\renewenvironment{itemize}
  { \old@itemize \singlespacing}
  { \endold@itemize }

%% Single spacing in equation arrays
\let\old@eqnarray\eqnarray
\let\endold@eqnarray\endeqnarray
\renewenvironment{eqnarray}
  { \begin{singlespace*} \begin{old@eqnarray} }
  { \end{old@eqnarray} \end{singlespace*} }


%% Headers: Put page number in upper-right hand corner.
\RequirePackage{fancyhdr}
\fancyhf{}  % Clear headers and footers
%%\fancyhead[RO,LE]{\thepage}
\fancyhead[R]{\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\headheight}{15pt}

%% No page number on first page of each chapter
\renewcommand\chapter{
  \clearpage
  \thispagestyle{empty}
  \pagestyle{fancy}
  \doublespacing
  \global\@topnum\z@
  \@afterindentfalse
  \secdef\@chapter\@schapter
}
%% Chapter headings should be centered, uppercase, and at the top of the page.
%% rws 01/08/2006 --centered mixed case no CHAPTER on front
\def\@makechapterhead#1{%
  { \parindent \z@ \raggedright \normalfont
    \centering
    \ifnum \c@secnumdepth >\m@ne  
        \huge \bfseries \thechapter \hspace{1em} #1\par\nobreak %\MakeUppercase{\@chapapp\space \thechapter} % revised rws --- 01/08/2006
        \par\nobreak
        %\vskip 20\p@
    \fi
    \interlinepenalty\@M
    %\Huge \bfseries #1\par\nobreak % revised rws --- 01/08/2006
    %\vskip 40\p@
  } }
\def\@makeschapterhead#1{%
  %\vspace*{50\p@}%
  { \parindent \z@ \raggedright
    \centering
    \normalfont
    \interlinepenalty\@M
     \Huge \bfseries  \MakeUppercase{#1}\par\nobreak 
    %\vskip 40\p@
  }}


%% ECU does not want large fonts.  Make them bold instead. % revised rws/2006
\renewcommand{\large}{\normalsize}
\renewcommand{\Large}{\normalsize}
\renewcommand{\LARGE}{\normalsize}
\renewcommand{\huge}{\normalsize}
\renewcommand{\Huge}{\normalsize}


\newcommand{\department}[1]{\gdef\@department{#1}}
\department{??DEPARTMENT??}
\newcommand{\school}[1]{\gdef\@school{#1}}
\school{}
\newcommand{\degree}[1]{\gdef\@degree{#1}}
\degree{??DEGREE??}
\newcommand{\advisor}[1]{\gdef\@advisor{#1}}
\advisor{??ADVISOR??}
\newcommand{\copyrightyear}[1]{\gdef\@copyrightyear{#1}}
\copyrightyear{??COPYRIGHTYEAR??}

\renewenvironment{abstract}{
  \clearpage
  \normalbaselines
  \chapter*{Abstract}
  \pagestyle{empty}
  \singlespacing
  \@author.  \MakeUppercase{\@title}. (Under the direction of
  \@advisor).  Department of \@department, \@date.

  \doublespacing
} {
  \clearpage
}

% Blank cover sheet
\newcommand{\coversheet}{ 
  \clearpage
  \thispagestyle{empty}
  \ 
  \clearpage }

\newcommand{\clearemptydoublepage}{
  \clearpage
  \thispagestyle{empty}
  \cleardoublepage
}


%% Member stuff based on dukethesis.cls:

% \@member{member name} -- internal macro to print a line to sign on, and the
%       name of a committee member (sole argument) below the line.
\newcommand{\@member}[2]{
  \MakeUppercase{#1}: & %
  \begin{center}%
  \raisebox{-8pt}[0pt][17pt]{\rule{3in}{.5pt}}\par    % Print line.
  \raisebox{0pt}[0pt][0pt]{#2}\par      % Print member name below.
  \end{center} %
  \tabularnewline
}

\newcounter{@members}           % Number of member macros defined so far.
\newcommand{\@membera}{\@member{Director of Thesis}{\@advisor}}
\setcounter{@members}{1}        % Advisor is always 1st member


% \member{member name} -- user macro to declare the name of a committee member.
%       May be used up to 7 times.  Should not be used for advisor.
\newcommand{\member}[2][Committee Member]{
  \addtocounter{@members}{1}    % Inc. num of members to include this new one.
  \ifcase\value{@members} 
    \typeout{Thesis format internal error.  Too few committee members.} \or
    \typeout{Thesis format internal error.  Advisor left off committee.} \or
    \newcommand{\@memberb}{\@member{#1}{#2}} \or
    \newcommand{\@memberc}{\@member{#1}{#2}} \or
    \newcommand{\@memberd}{\@member{#1}{#2}} \or
    \newcommand{\@membere}{\@member{#1}{#2}} \or
    \newcommand{\@memberf}{\@member{#1}{#2}} \or
    \newcommand{\@memberg}{\@member{#1}{#2}} \or
    \newcommand{\@memberh}{\@member{#1}{#2}} 
  \else
    \typeout{Error using thesis format.  Too many committee members.}
  \fi
}

\newcommand{\departmentchair}[1] {
  \member[Chair of the Department of \@department]{#1}
}
\newcommand{\dean}[1] {
  \member[Dean of the \newline Graduate School]{#1}
}




%% Title page
\renewcommand{\maketitle}{
  \clearpage
    \setcounter{page}{1}  % ``The title page and signature page together
                          % count as the first page of the prefatory material''
    \pagenumbering{roman}

    \doublespacing
    \begin{center}

      { \MakeUppercase{\@title} \par}  % NO bold rws 01/08/2006
      %{\bfseries \MakeUppercase{\@title} \par}  

    \vfill

      A Thesis

      Presented to

      The Faculty of the Department of \@department

      East Carolina University \@school

    \vfill

      In Partial Fulfillment

      of the Requirements for the Degree

      \@degree \ in \@department

    \vfill

      by

      \@author

      \@date
    \end{center}
  \clearpage
}


%% Copyright page
%% Added 12/2009
\newcommand{\makecopyright}{
  \clearpage
    \setcounter{page}{1}  % ``The title page and signature page together
                          % count as the first page of the prefatory material''
                          % Assuming copyright page is also page 1, though no guidance received on this
    \pagenumbering{roman}

    \doublespacing
    \begin{center}
    
    \par
    \null
    \vfill

      Copyright \@copyrightyear, \@author

          \end{center}
          \vfill
  \clearpage
}

\newcounter{@membersprinted}

%% Signature page
\newcommand{\makesignature}{
  \clearpage
    \setcounter{page}{1}  % ``The title page and signature page together
                          % count as the first page of the prefatory material''
    \pagenumbering{roman}

    \doublespacing
    \begin{center}

      %\textbf{\MakeUppercase{\@title}}
      \MakeUppercase{\@title}
      
      \vfill

      by\\
      \@author
    \end{center}
    \singlespacing

      \vfill

      \begin{center}
	\MakeUppercase{Approved By:}
      \end{center}
      \noindent
      \begin{tabular}{p{2.5in}p{3in}}%
	  \setcounter{@membersprinted}{0}%
	  \@whilenum \value{@membersprinted} < \value{@members} \do {%
            \stepcounter{@membersprinted}%
            \ifcase\value{@membersprinted}%
              \typeout{Thesis style--internal error printing members.} \or%
              \@membera \or%
              \@memberb \or%
              \@memberc \or%
              \@memberd \or%
              \@membere \or%
              \@memberf \or%
              \@memberg \or%
              \@memberh%
            \else \typeout{Thesis style--internal error printing members.}%
            \fi %
          }%
      \end{tabular}
  \clearpage
}

\newcommand{\pchapter}[1] { %% A preliminary chapter
  \chapter*{#1}
  \thispagestyle{empty}
  \pagestyle{fancy}
  \addcontentsline{toc}{chapter}{#1}
}



\RequirePackage[titles]{tocloft}

\tocloftpagestyle{empty}


\renewcommand{\cftchapdotsep}{\cftdotsep}
\renewcommand{\cftchappresnum}{} 
\renewcommand{\cftchappagefont}{}
%\addtolength{\cftchapnumwidth}{1 in}

%\renewcommand{\cftchapfont}{\bfseries}
 \renewcommand{\cftchapfont}{}  %rws--Jan 12, 2006 no bold for toc entries
\setcounter{tocdepth}{4}


\renewcommand{\tableofcontents}{
  \clearpage
  \normalbaselines
  \chapter*{Table of Contents}
  \pagestyle{empty}
  \markboth{CONTENTS}{CONTENTS}
  \@starttoc{toc}
  \clearpage
}

%------

\renewcommand{\listoftables}{
  \normalbaselines
  \pchapter{LIST OF TABLES}
  \markboth{LIST OF TABLES}{LIST OF TABLES}
  \@starttoc{lot}
}


\renewcommand{\listoffigures}{
  \normalbaselines
  \pchapter{LIST OF FIGURES}
  \markboth{LIST OF FIGURES}{LIST OF FIGURES}
  \@starttoc{lof}
}

%\def\l@figure{{\protect\addvspace{14.5pt}}\@dottedtocline{1}{1.5em}{2.3em}}
%\def\l@figure{\@dottedtocline{1}{1.5em}{2.3em}}
%\let\l@table\l@figure

\newcommand{\chapters} {
  \clearpage
  \setcounter{page}{1}
  \pagenumbering{arabic}
}


%% Bibliography should be single spaced, and placed in the table of contents
%% It should use an APA-like format.
\renewcommand{\bibname}{BIBLIOGRAPHY}
\RequirePackage[authoryear,sort]{natbib}
\bibliographystyle{apalike}
\renewenvironment{thebibliography}[1]
     {\chapter*{\bibname}%
      \singlespacing %
      \addcontentsline{toc}{chapter}{BIBLIOGRAPHY}%
      \@mkboth{\MakeUppercase\bibname}{\MakeUppercase\bibname}%
      \list{\@biblabel{\@arabic\c@enumiv}}%
           {\settowidth\labelwidth{\@biblabel{#1}}%
            \leftmargin\labelwidth
            \advance\leftmargin\labelsep
            \@openbib@code
            \usecounter{enumiv}%
            \let\p@enumiv\@empty
            \renewcommand\theenumiv{\@arabic\c@enumiv}}%
      \sloppy
      \clubpenalty4000
      \@clubpenalty \clubpenalty
      \widowpenalty4000%
      \sfcode`\.\@m}
     {\def\@noitemerr
       {\@latex@warning{Empty `thebibliography' environment}}%
      \endlist}
