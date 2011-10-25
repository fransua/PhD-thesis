(TeX-add-style-hook "main"
 (lambda ()
    (LaTeX-add-bibliographies
     "biblio/bibliography")
    (LaTeX-add-labels
     "intro"
     "chap:dna_struct"
     "chap:untb_genomes"
     "chap:gssa"
     "chap:tools"
     "conclusion")
    (TeX-run-style-hooks
     "nomencl"
     "paralist"
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
     "openany"
     "tex_source/Introduction/introduction"
     "tex_source/Chapters/dna_struct"
     "tex_source/Chapters/untb_genomes"
     "tex_source/Chapters/gssa"
     "tex_source/Chapters/tools"
     "tex_source/Conclusion/conclusion")))

