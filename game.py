from meet import*
import math

cells = []
for i in range(20):
	ball = {"radius": random.randint(10,40), "x":random.randint(0,100),"y":random.randint(0,100), "dy":random.randint(-3,3), "dx":random.randint(-3,3), "color":"pink"}
	circle = create_cell(ball)
	cells.append(circle)

user = {"radius": 20, "x":0 ,"y":0 ,"dy":1 , "dx":1}
player = create_cell(user)

def borders(cells):
	h = get_screen_height()
	w = get_screen_width()      
	for cell in cells:	
		x = cell.xcor()
		y = cell.ycor()
		r = cell.get_radius()
		if x+r > w or x-r < -w:
			cell.dx = -cell.dx
		if y+r > h or y-r < -h:
			cell.dy = -cell.dy

def user(player):
	x, y = get_user_direction(player)
	player.set_dx(x)
	player.set_dy(y)


cells.append(player)

def eat(player, cells):
	x = player.xcor()
	y = player.ycor()
	r = player.get_radius()
	for cell in cells:
		cellx = cell.xcor()
		celly = cell.ycor()
		cellr = cell.get_radius()

		if (math.sqrt(((y - celly)**2) + ((x - cellx)**2))) <r+cellr and cell != player:
			player.set_radius(r+cellr/2)
			cell.set_radius(0)




while True:
	move_cells(cells)
	borders(cells)
	user(player)
	eat(player, cells)

