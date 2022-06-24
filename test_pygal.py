import pygal
from decimal import Decimal

r = 255 - 0.99*255
g = 255 * 0.99
b = 0
c = (r, g, b)

color = 'rgb' + str(c)

print(color)

xy_chart = pygal.XY(stroke=False)
xy_chart.title = 'A Made Up Correlation Between Search Engines'
xy_chart.add("A", [
			 {'value': (5, 5), 'label': '99% success', 'color': color}, \
			 {'value': (3, 3), 'label': '17% success9', 'color': 'green'}
			 ])
xy_chart.render_to_file('test.svg')


