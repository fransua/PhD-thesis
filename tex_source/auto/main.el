(TeX-add-style-hook "main"
 (lambda ()
    (LaTeX-add-bibliographies
     "../biblio/bibliography")
    (TeX-run-style-hooks
     "geometry"
     "tocloft"
     "titles"
     "inputenc"
     "latin1"
     "hyperref"
     "graphicx"
     "latex2e"
     "scrbook11"
     "scrbook"
     "spanish"
     "a4paper"
     "11pt"
     "openany")))

