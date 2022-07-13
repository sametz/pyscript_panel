"""This module contains the Python code for the first (simple) app.

Testing how to keep the Python code in separate .py modules, and import them
into the .html document.
"""

import calendar

import panel as pn

pn.extension(sizing_mode="stretch_width")

month = pn.widgets.IntSlider(start=1, end=12, name='Month')


def callback(new):
    c = calendar.HTMLCalendar(calendar.SUNDAY)
    return c.formatmonth(2022, new)


pn.Column(
    "# Panel PyScript Calendar Example",
    month,
    pn.bind(callback, month),
).servable(target='simple_app');  # keeping training comma for now
