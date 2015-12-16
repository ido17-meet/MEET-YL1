from meet import*
import math
import time



colors = ["red","pink", "green", "blue", "brown", "maroon"]
cells = []
for i in range(20):
	ball = {"radius": random.randint(5,40), "x":random.randint(0,100),"y":random.randint(0,100), "dy":random.randint(-3,3), "dx":random.randint(-3,3), "color":colors[random.randint(0, len(colors)-1)]}
	circle = create_cell(ball)
	cells.append(circle)

for i in range(30):
	ball = {"radius": 5, "x":get_random_x(),"y":get_random_y(), "dy":0, "dx":0, "color": ""}
	circle = create_cell(ball)
	cells.append(circle)

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


def eat(player, cells):
	x = player.xcor()
	y = player.ycor()
	r = player.get_radius()
	for cell in cells:
		cellx = cell.xcor()
		celly = cell.ycor()
		cellr = cell.get_radius()

		if (math.sqrt(((y - celly)**2) + ((x - cellx)**2))) <r+cellr and cell != player and r>cellr:
			player.set_radius(r+cellr/2)
			cell.goto(get_random_x(),get_random_y())
				 
		elif (math.sqrt(((y - celly)**2) + ((x - cellx)**2))) <r+cellr and cell != player:
			cellr = cellr + r
			r = 0
			write("Game Over!", move=False, align="left", font=("Arial", 100, "bold"))
			time.sleep(3)
			bye()
			quit()
		if r>get_screen_width()*1.5:
			pencolor("white")
			goto(0,0)
			write("you've won!", move=False, align="center", font=("Arial", 100, "bold"))
			time.sleep(3)
			bye()
			quit()

user_dictionary = {"radius": 12, "x":-150 ,"y":10 ,"dy":1 , "dx":1, "color":"orange"}
player = create_cell(user_dictionary)
cells.append(player)

def points():
	clear()
	goto(-get_screen_width()+20, get_screen_height()-(get_screen_height()/4))
	write((str(player.get_radius())+" points")[:5],align="left",font=("Arial", 20, "bold"))


while True:
	move_cells(cells)
	borders(cells)
	user(player)
	eat(player, cells)
	points()
