from meet import*
import time

cells = []

for i in range(50):
	ball = {"radius": random.randint(0,90), "x":random.randint(0,100),"y":random.randint(0,100), "dy":random.randint(-5,5), "dx":random.randint(-5,5)}
	circle = create_cell(ball)
	cells.append(circle)
		

def borders(cells):
	h = get_screen_hight()
	w = get_screen_width()
	for cell in cells:
		x = xcor()
		y = ycor()
		r = circle.get_radius()
		if x+r > w:
			ball.set_dx(-dx)
		if y+r > h:
			ball.set_dy(-dy)


while True:
	move_cells(cells)
	borders(cells)

