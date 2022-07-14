"""Code for a simple nmr app will go here."""

import panel as pn


pn.extension(sizing_mode="stretch_width")
intro = pn.pane.Markdown("""
This app will provide a simple example of an NMR simulation.
""").servable(target='placeholder')
