import time
import random
import turtle as t
from player import Player
from alien import Alien
from bullet import Bullet


player_bullets = []
enemy_bullets = []
ready_to_fire = True
player_points = 0
player_lives = 3


def update_text():
    writer.clear()
    writer.goto(-380, 250)
    writer.write(f"POINTS: {player_points}", move=True, font=("Courier", 32, "normal"))

    writer.goto(170, 250)
    writer.write(f"LIVES: {player_lives}", move=True, font=("Courier", 32, "normal"))


def fire_player():
    global ready_to_fire
    if ready_to_fire:
        player_bullet = Bullet(player.xcor(), player.ycor() + 40)
        player_bullets.append(player_bullet)
        ready_to_fire = False


def fire_enemy():
    chance = random.randint(1, 50)
    if len(aliens) > 8:
        enemy = random.randint(0, 7)
    else:
        enemy = random.randint(0, len(aliens))
    if chance == 24:
        enemy_bullet = Bullet(aliens[-enemy].xcor(), aliens[-enemy].ycor() - 20)
        enemy_bullet.vel_y *= -1
        enemy_bullets.append(enemy_bullet)


def game_over():
    global game_on
    writer.goto(-130, -50)
    writer.write("GAME OVER", move=True, font=("Courier", 32, "normal"))
    game_on = False


def win():
    global game_on
    writer.goto(-80, -50)
    writer.write("YOU WIN", move=True, font=("Courier", 32, "normal"))
    game_on = False


t.addshape("player.gif")
t.addshape("alien1.gif")

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player("player.gif")

aliens = []

x_pos = -180
y_pos = 200
points = 15

writer = t.Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)
writer.color("white")
update_text()

for k in range(4):
    for i in range(8):
        new_alien = Alien("alien1.gif", points, x_pos, y_pos)
        x_pos += 50
        aliens.append(new_alien)
    x_pos = -180
    y_pos -= 30
    points += 5

screen.listen()

screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkeypress(fire_player, "space")

game_on = True
prev_time = time.time()
next_time = prev_time + 0.2


while game_on:
    screen.update()
    time.sleep(0.025)

    if aliens:
        fire_enemy()

    if time.time() >= next_time:
        prev_time = time.time()
        next_time = prev_time + 0.2
        for alien in aliens:
            alien.move()
            if alien.xcor() <= -380 or alien.xcor() >= 380:
                for alien1 in aliens:
                    alien1.vel_x *= -1
                    alien1.goto(alien1.xcor(), alien1.ycor() - 30)

    if player_bullets:
        for bullet in player_bullets:
            bullet.move()

            try:
                for alien in aliens:
                    if bullet.distance(alien) < 30:
                        player_points += alien.points
                        alien.goto(3000, 3000)
                        aliens.remove(alien)
                        bullet.goto(3000, 3000)
                        player_bullets.remove(bullet)
                        ready_to_fire = True
                        update_text()

                    elif bullet.ycor() > 320:
                        if player_bullets:
                            bullet.hideturtle()
                            player_bullets.remove(bullet)
                            ready_to_fire = True
            except ValueError:
                print("Too fast")

    if enemy_bullets:
        for bullet in enemy_bullets:
            bullet.move()

            if bullet.distance(player) < 20:
                player.goto(0, player.ycor())
                player_lives -= 1
                update_text()

    if player_lives <= 0:
        game_over()

    if not aliens:
        win()
screen.mainloop()
