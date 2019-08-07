(TeX-add-style-hook "these"
 (lambda ()
    (LaTeX-add-bibliographies
     "library")
    (TeX-add-symbols
     '("mc" 3))
    (TeX-run-style-hooks
     "wasysym"
     "multicol"
     "fontenc"
     "T1"
     "times"
     "wrapfig"
     "inputenc"
     "utf8"
     "babel"
     "english"
     "latex2e"
     "beamer10"
     "beamer"
     "table")))

