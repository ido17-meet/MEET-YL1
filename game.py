from meet import*
import math
import time

#To-Do List:
#bacground
#buttons+
#timer
#menues
#make the game harder

def start():
	x=3
	goto(0,0)
	hideturtle()
	while x>0:
		clear()
		time.sleep(1)
		write(x, move=False, align="center", font=("Arial", 70, "normal"))
		x-=1

colors = ["red","pink", "green", "blue", "brown", "maroon"]
cells = []
#make the other cells
for i in range(20):
	ball = {"radius": random.randint(5,70), "x":random.randint(0,100),"y":random.randint(0,100), "dy":random.randint(-3,3), "dx":random.randint(-3,3), "color":colors[random.randint(0, len(colors)-1)]}
	circle = create_cell(ball)
	cells.append(circle)
#make the "food" cells
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
		distance = (math.sqrt(((y - celly)**2) + ((x - cellx)**2)))
		if distance <r+cellr and cell != player and r>cellr:
			player.set_radius(r+cellr/2)
			cell.goto(get_random_x(),get_random_y())
		
		elif distance <r+cellr and cell != player :
			cellr = cellr + r
			r = 0
			goto(0,0)
			write("Game Over!", move=False, align="center", font=("Arial", 100, "bold"))
			time.sleep(3)
			bye()
			quit()
		if r>get_screen_width()*1.2:
			pencolor("white")
			goto(0,0)
			write("you've won!", move=False, align="center", font=("Arial", 100, "bold"))
			time.sleep(3)
			bye()
			quit()
		if distance <r+cellr and cell != player and r>cellr and r>70:
			player.set_radius(r+cellr/2)
			cell.goto(get_random_x(),get_random_y())
			cellr = cellr*1.5

#make the players cell
user_dictionary = {"radius":9 , "x":-150 ,"y":10 ,"dy":1 , "dx":-5, "color":"orange"}
player = create_cell(user_dictionary)
cells.append(player)

def points():
	clear()
	goto(-get_screen_width()+20, get_screen_height()-(get_screen_height()/4))
	write((str(player.get_radius())[:4])+" points",align="left",font=("Arial", 20, "bold"))

start()
while True:
	user(player)
	move_cells(cells)
	borders(cells)
	eat(player, cells)
	points()
