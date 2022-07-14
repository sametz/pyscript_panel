"""Code for a simple nmr app will go here."""

import panel as pn
pn.extension(sizing_mode="stretch_width")
import holoviews as hv
hv.extension('bokeh', width=100)

from dnmr import DnmrAB, dnmr_AB

intro = pn.pane.Markdown("""
This app will provide a simple example of an NMR simulation.\n
va, vb = the chemical shifts for nuclei A and B.\n
J = the coupling constant.
k = the rate constant for the exchange process.
w = the line width in Hz.
""").servable(target='placeholder')


def abplot(va, vb, J, k, w):
    x, y = dnmr_AB(va, vb, J, k, w)
    return hv.Curve(zip(x, y))

title = pn.panel('#DNMR Simulation: Two Coupled Nuclei')

# defaults = ("va=165, vb=135, J=12, k=12, w=0.5")
app = pn.interact(abplot, va=165, vb=135, J=12, k=(0.001, 1000, 0.1, 12), w=(0.1, 10, 0.1, 0.5))
row = pn.Column(app[0], app[1])
combo = pn.Column(title, row)

combo.servable(target="simple_app");
