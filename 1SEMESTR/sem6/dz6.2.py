from random import randrange as rnd, choice
from tkinter import *
import math
import time

class Ball:
    """ Класс Ball описывает мяч. """

    def __init__(self, x=40, y=450):
        """ Конструктор класса Ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def set_coords(self):
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """ Метод move описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения 
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # Gravity constant
        g = 1.5
        
        # Update position based on velocity
        self.x += self.vx
        self.y -= self.vy  # y axis is inverted in tkinter (0 at top)
        
        # Update velocity with gravity
        self.vy -= g
        
        # Air resistance
        self.vx *= 0.98
        self.vy *= 0.98
        
        # Check for collision with walls
        if self.x - self.r < 0 or self.x + self.r > 800:
            self.vx = -self.vx * 0.8  # Bounce with energy loss
            self.x = max(self.r, min(800 - self.r, self.x))
            
        if self.y - self.r < 0 or self.y + self.r > 600:
            self.vy = -self.vy * 0.8  # Bounce with energy loss
            self.y = max(self.r, min(600 - self.r, self.y))
            
        # Update the ball's position on canvas
        self.set_coords()
        
        # Decrease live time
        if self.y >= 590:
            self.live -= 1

    def hittest(self, ob):
        """ Функция проверяет сталкивалкивается ли данный объект с целью, описываемой в объекте ob.

        Args:
            ob: Объект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ob is None:
            return False
        # Calculate distance between centers
        distance = math.sqrt((self.x - ob.x)**2 + (self.y - ob.y)**2)
        # Check if distance is less than sum of radii
        return distance <= (self.r + ob.r)


class Gun:
    """ Класс gun описывает пушку. """
    
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """ Выстрел мячом происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.x, self.y)
        new_ball.r += 5
        self.an = math.atan2((self.y - event.y), (event.x - self.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)  # Negative because y axis is inverted
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=None):
        """ Прицеливание. Зависит от положения мыши.
        """
        if event:
            self.an = math.atan2((self.y - event.y), (event.x - self.x))
        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')
        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y - max(self.f2_power, 20) * math.sin(self.an))

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')


class Target:
    """ Класс target описывает цель. """
    
    def __init__(self):
        self.points = 0
        self.live = 1
        # Create the target when object is created
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.x = rnd(600, 780)
        self.y = rnd(300, 550)
        self.r = rnd(2, 50)
        self.color = 'red'
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

    def hit(self, points=1):
        """ Попадание шарика в цель. """
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text=self.points)


# Global variables
root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

t1 = Target()
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = Gun()
bullet = 0
balls = []


def new_game(event=None):
    global t1, screen1, balls, bullet
    # Reset target
    t1.new_target()
    t1.live = 1
    
    # Reset bullets
    bullet = 0
    balls = []
    
    # Bind events
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    # Main game loop
    while t1.live or balls:
        # Move all balls
        for b in balls:
            b.move()
            # Check for hit
            if b.hittest(t1) and t1.live:
                t1.live = 0
                t1.hit()
                canv.bind('<Button-1>', lambda e: None)
                canv.bind('<ButtonRelease-1>', lambda e: None)
                canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        
        # Update canvas
        root.update()
        time.sleep(0.03)
        
        # Update gun
        g1.targetting()
        g1.power_up()
        
        # Remove dead balls
        balls = [b for b in balls if b.live > 0]
    
    # Game over
    canv.itemconfig(screen1, text='')
    root.after(750, new_game)


#Start the game
new_game()
mainloop()
