#!/usr/bin/python
"""
20 May 2012


"""

__author__  = "Francois-Jose Serra"
__email__   = "francois@barrabin.org"
__licence__ = "GPLv3"
__version__ = "0.0"

from ete_dev import EvolTree
from ete_dev import TreeStyle
from ete_dev.treeview.layouts import evol_layout
from ete_dev.evol.model import colorize_rst
from ete_dev.treeview.faces import SequencePlotFace
            
tree = EvolTree("(Orangutan,Human,Chimp);")
tree.link_to_alignment("""
>Chimp
CCC GCA CGA TGG CTC AAT GTA AAG TTA AGA TGC GAA TTG AGA ACA CTA AAA AAA
TTG GGA CTG GAC GGC TAC AAG GCA GTA AGT CAA TAC GTT AAA GGT CGT GCG ATT
>Orangutan
GAT GCA CGA TGG ATC AAT CCA AAG TTA AGA TGC GAA TTG AGA ACT CTG AAA AAA
TTG GGA CTG GAC GGC TAC AAG GCA GCA AGT CAA TAC GTT AAA GGT CGT AGC TCT
>Human
TAC GCA CGA TGG CTC AAC GTA AAA TTA AGA TGT GAA TTA AGG ACG CTC AAA AAA 
TTG GGA CTG GAC GGC TAC AAG GCA GTA AGT CAA TAC GTT CAA GGT CGT GCC AGT
""")

try:
    #tree.run_model("fb")
    #tree.run_model("M2")
    #tree.run_model("M1")
    #tree.run_model("SLR")
    tree.link_to_evol_model("/tmp/ete2-codeml/fb/out" , "fb")
    tree.link_to_evol_model("/tmp/ete2-codeml/M2/out" , "M2")
    tree.link_to_evol_model("/tmp/ete2-codeml/SLR/out", "SLR")
    m2 = tree.get_evol_model("M2")
    m2.set_histface(up=False)
    slr = tree.get_evol_model("SLR")
except:
    pass

#print tree.get_most_likely("M2", "M1")
print m2.sites['BEB']['pv'][0]
ts = TreeStyle()
ts.tree_width = 95
ts.layout_fn = evol_layout
ts.aligned_header.add_face(SequencePlotFace(m2.sites['BEB']['w'], hlines=[0.3,1.0],
                                            kind='bar', ylim=(0,2), ylabel=u'Omega (\u03c9)',
                                            colors=colorize_rst(m2.sites['BEB']['pv'],"M2", 
                                                                m2.sites['BEB']["class"]),
                                            header='Omega shape over sites, model M2a',
                                            hlines_col=['#979797','#454545']), 1)

ts.aligned_foot.add_face(SequencePlotFace(slr.sites['SLR']['w'], hlines=[0.3,1.0],
                                          kind='bar', ylim=(0,2), ylabel=u'Omega (\u03c9)',
                                          colors=colorize_rst(slr.sites['SLR']['pv'],"SLR", 
                                                              slr.sites['SLR']["class"]),
                                          header='Omega shape over sites, model SLR',
                                          hlines_col=['#979797','#454545']), 1)

#tree.render('/home/francisco/Documents/these/figures/tools/sample_fb_M2_SLR.pdf', h=5000, tree_style=ts)
# The interactive features are only available using the GUI
#tree.show(tree_style=ts,histfaces=['M2'])

tree.show(tree_style=ts)

tree.mark_tree ([(tree & 'Orangutan')._nid], marks=['#1'])
print tree.write()
tree.run_model("b_free")
tree.mark_tree ([(tree & 'Orangutan')._nid], marks=[''])
print tree.write()
tree.run_model("M0")
print tree.get_most_likely("b_free", "M0")


