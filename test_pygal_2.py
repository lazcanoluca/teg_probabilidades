import pygal
from pygal import Config

config = Config()
config.show_legend = False
config.human_readable = True
config.fill = True

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'Probabilidad De Victoria Contiendas Reiteradas TEG.'
xy_chart.add = ((0,1))

xy_chart.render_to_file('test_15.svg')
