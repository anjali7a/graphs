from bokeh.plotting import figure, output_file, show
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
y = (175, 5, 190, 5, 205, 5, 200, 5, 199)
output_file( "lines.html" )
p = figure(title="simple line example", x_axis_label='y')
p.line(x, y, legend="temp.", line_width=2)
show(p)

