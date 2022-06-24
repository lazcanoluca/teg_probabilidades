import pygal
from pygal import Config
from pygal.style import DarkStyle
from random import randint
from decimal import Decimal

def tirar_dado(lados=6):
	return randint(1, lados)

def derrota():
	"""Condiciones de derrota."""
	
def tiro(fichas):
	"""Tira 1, 2 o 3 dados en función de las fichas."""
	
	if fichas >= 3:
		tiro = sorted([tirar_dado(), tirar_dado(), tirar_dado()], reverse = True)
	elif fichas == 2:
		tiro = sorted([tirar_dado(), tirar_dado()], reverse = True)
	elif fichas == 1:
		tiro = [tirar_dado()]

	return tiro
	
def contienda(fichas_ataque, fichas_defensa):
	"""Contienda recursiva."""
	
	#print("Fichas iniciales ataque: " + str(fichas_ataque))
	#print("Fichas iniciales defensa: " + str(fichas_defensa) + "\n")
	
	while fichas_ataque > 0 and fichas_defensa > 0:
		
		tiro_ataque = tiro(fichas_ataque)
		#print("\nDados del atacante: " + str(tiro_ataque))
		tiro_defensa = tiro(fichas_defensa)
		#print("Dados del defensor: " + str(tiro_defensa))
		
		dados_comparar = min(len(tiro_ataque), len(tiro_defensa))
		#print("Juegan " + str(dados_comparar) + " dados.\n")
		
		for dado in range(dados_comparar):
			if tiro_ataque[dado] > tiro_defensa[dado]:
				fichas_defensa -= 1
			elif tiro_ataque[dado] <= tiro_defensa[dado]:
				fichas_ataque -= 1
		
		#print("Al atacante le quedan: " + str(fichas_ataque))
		#print("Al defensor le quedan: " + str(fichas_defensa))
	
	resto = [fichas_ataque, fichas_defensa]
	#print(resto)
	
	return resto

def color(coef__vic):
	r = int(255 - coef_vic * 100)
	g = int(255 * coef_vic)
	c = (r, g, 0)
	color = 'rgb' + str(c)
	
	return color

def coeficiente_victoria(ganadas, x):
	coeficiente_victoria = round(Decimal(ganadas / x), 3)
	return coeficiente_victoria

def porcentaje_victoria(coef_vic):
	"""Devuelve string del porcentaje victoria."""
	x = coef_vic
	porcentaje_victoria = str(round((coef_vic * 100), 1)) + '%'
	return porcentaje_victoria
	
	
#def imprimir(lista):
#	xy_chart = pygal.XY(show.legend=False, stroke = False)
#	xy_chart.title = 'Probabilidad De Victoria Contiendas Reiteradas TEG.'
#	xy_chart.add = (lista)
	
lista = []
x = 100

for rango_ataque in range(1, 41):
	for rango_defensa in range(1, 41):
		perdidas = 0
		ganadas = 0
		restantes = 0
		for veces in range(x):
			resto = contienda(rango_ataque, rango_defensa)
			if resto[0] == 0:
				perdidas += 1
			elif resto[1] == 0:
				ganadas += 1
				restantes =+ resto[0]
			rest = str(restantes)
		
	#	print('Ganadas: ' + str(ganadas))
	#	print('Perdidas: ' + str(perdidas))
		#print(rest)
		coef_vic = coeficiente_victoria(ganadas, x)
		porc_gan = porcentaje_victoria(coef_vic)		
		prom_restantes = str(restantes / x)
		#print(prom_restantes)
		label = porc_gan
		colour = color(coef_vic)
		lista.append({'value': (rango_ataque, rango_defensa),\
			 'label': porc_gan, \
			 'color': colour})
			 
	#	print('x = ' + str(rango_ataque))
	#	print('y = ' + str(rango_defensa))
	#	print('Porcentaje victoria: ' + str(porc_gan))
	#	print('Ejércitos restantes promedio: ' + str(prom_restantes) + '\n')
				

print(lista)
#contienda(3,3)

xy_chart = pygal.XY(stroke=False, dots_size=5, show_y_guides=False, show_legend=False, style=DarkStyle)
xy_chart.title = 'Probabilidad De Victoria Contiendas Reiteradas TEG.'
#xy_chart.add = ("A", lista)
xy_chart.add("A", lista)
xy_chart.render_to_file('tegtest.svg')
