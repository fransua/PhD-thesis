(TeX-add-style-hook "template"
 (lambda ()
    (TeX-add-symbols
     '("member" ["argument"] 1)
     '("pchapter" 1)
     '("dean" 1)
     '("departmentchair" 1)
     '("copyrightyear" 1)
     '("advisor" 1)
     '("degree" 1)
     '("school" 1)
     '("department" 1)
     "coversheet"
     "clearemptydoublepage"
     "makecopyright"
     "makesignature"
     "chapters")
    (TeX-run-style-hooks
     "natbib"
     "authoryear"
     "sort"
     "tocloft"
     "titles"
     "fancyhdr"
     "setspace"
     "vmargin"
     "calc"
     "rep12"
     "report"
     "letterpaper"
     "onecolumn"
     "12pt")))

