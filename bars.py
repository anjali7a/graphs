from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.palette import Spectral6

output_file("bars.html")
name = ['Dhyana', 'Smaran', 'Lali', 'Anna', 'Aramaia']
ages = [7, 11, 7, 9, 9]
colors = Spectral6

p = figure(x_range=name, plot_height=250, title="Ages",
           toolbar_location=None, tools="")

p.vbar(x=name, top=ages, width=0.8)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
