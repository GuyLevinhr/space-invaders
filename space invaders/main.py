import pygame
import random
import tkinter as tk
from tkinter import messagebox

# Class For Colors
class ColorClass:
    def __init__(self):
        self.colors = { "white": (255, 255, 255),
                        "red": (255, 0, 0),
                        "yellow": (255, 255, 0),
                        "purple": (205, 0, 136),
                        "black": (0, 0, 0),
                        "green": (50, 205, 50)
                       }


# Class Cell is the basic object that all other class made from
class CellClass:
    def __init__(self, x, y, color="white"):
        global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

        self.x = x
        self.y = y
        self.color = colors.colors[color]

    # Draw Single cell
    def draw(self):
        global colors, surface, width, rows
        dis = width // rows

        # Draw on surface
        pygame.draw.rect(surface, self.color, (self.x*dis, self.y*dis, dis, dis))


# Class fire for Shoot
class FireClass:
    def __init__(self, x, y, isSpaceshipFire=1):
        global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
        self.x = x
        self.y = y
        self.IsSpaceshipFire = isSpaceshipFire


        if isSpaceshipFire == 1:
            # Spaceship Fire color
            color = "red"
        else:
            # Monster Fire color
            color = "purple"

        # create the first cell
        head_cell = CellClass(x, y, color)

        self.cells = [head_cell]

        # add more 2 cell to Fire cell list
        for i in range(2):
            cell = CellClass(x, y - i, color)
            self.cells.append(cell)

    # Draw Single Fire
    def draw(self):
        for cll in self.cells:
            cll.draw()


# Class Spaceship
class SpaceshipClass:
    def __init__(self, x, y):
        global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
        self.x = x
        self.y = y
        self.cells = []

        # list of indication 1/0 to draw the Spaceship
        data = [
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]

        # Run over the data and create Cells list to  Spaceship
        for r, row in enumerate(data):
            for c, iscell in enumerate(row):
                if iscell:
                    cell = CellClass(x + c, y + r, "white")
                    self.cells.append(cell)

        # Centralized the head of the Spaceship
        self.x = x + 4
        self.y = y + 5

    # Draw Spaceship
    def draw(self):
        # run over all Cells list and draw
        for cll in self.cells:
            cll.draw()


# Class Monster
class MonsterClass:
    def __init__(self, x, y):
        global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
        self.x = x
        self.y = y
        self.cells = []

        # list of indication 1/0 to draw the Monster
        data = [
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 1],
            [1, 0, 0, 1, 1, 1, 0, 0, 1],
            [1, 1, 0, 0, 0, 0, 0, 1, 1]
        ]

        # Run over the data and create Cells list to  Monster
        for r, row in enumerate(data):
            for c, iscell in enumerate(row):
                if iscell:
                    cell = CellClass(x+c, y+r, "yellow")
                    self.cells.append(cell)

    # Draw Monster
    def draw(self):
        # run over all Cells list and draw
        for cll in self.cells:
            cll.draw()

    # Make the Monster move
    def move(self,mX,mY):
        for cll in self.cells:
            cll.x += mX
            cll.y += mY


# Class Block
class BlockClass:
    def __init__(self, x, y):
        global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
        self.x = x
        self.y = y
        self.cells = []

        # list of indication 1/0 to draw the Block
        data = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
        ]

        # Run over the data and create Cells list to  Block
        for r, row in enumerate(data):
            for c, iscell in enumerate(row):
                if iscell:
                    cell = CellClass(x+c, y+r, "green")
                    self.cells.append(cell)

    # Draw Monster
    def draw(self):
        for cll in self.cells:
            cll.draw()


# Create Monsters
def CreateMonsters():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
    # Calc the distance between Monsters
    dis = width // rows * 2

    # Create the rows and columns of many Monsters
    for row in range(11):
        for cell in range(5):
            x = row * 15 + dis
            y = cell * 15 + dis
            monster = MonsterClass(x, y)
            monsters.append(monster)


# Monsters Dance
def MonstersDance(move):
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

    # Run over all Monsters and change the position
    for monste in monsters:
        monste.move(move,move)


# Create Blocks
def CreateBlocks():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

    # Calc the distance between Blocks
    dis = width // rows * 2

    # Create the row of 5 Blocks
    for row in range(5):
        x = row * 31 + dis*2
        y = 105
        block = BlockClass(x, y)
        blocks.append(block)


# Monster fire
def MonsterFire():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
    # Number of Monster
    MonsterCount = len(monsters) - 1

    # Choose random Monster that will fire
    MonsterShoot = random.randint(0,MonsterCount)

    monster = monsters[MonsterShoot]

    # Make Fire
    fire = FireClass(monster.x + 4, monster.y, isSpaceshipFire=0)

    fires.append(fire)


# Spaceship move and fire
def SpaceshipMoveAndFire():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Get pressed keys
    keys = pygame.key.get_pressed()

    # Move Spaceship left
    if keys[pygame.K_LEFT] and 7 < spaceship.x:
        for c in spaceship.cells:
            c.x = c.x - 3
        spaceship.x -= 3

    # Move Spaceship right
    elif keys[pygame.K_RIGHT] and spaceship.x < 168:
        for c in spaceship.cells:
            c.x = c.x + 3
        spaceship.x += 3

    # Spaceship Shoot
    if keys[pygame.K_SPACE]:
        fire = FireClass(spaceship.x, spaceship.y - 2)
        fires.append(fire)


# Fire Move
def FireMove():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

    # The numbers of cell that fire move  every iteration
    step = 3

    # Run over all Fire list and move uo or down
    for fire in fires:
        if fire.IsSpaceshipFire == 1:
            firesStep = step
        else:
            firesStep = step * -1

        for c in fire.cells:
            c.y = c.y - firesStep
        fire.y -= firesStep


# The hit Func
def Boom():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life

    # Run over all Spaceship Fire and check if the fire hit the  monsters
    for fire in filter(lambda x: x.IsSpaceshipFire == 1, fires):
        hit = 0
        for monster in monsters:
            for cell in monster.cells:
                if fire.x == cell.x and fire.y == cell.y:
                    # if fire hit the monster remove the monster and the fire
                    monsters.remove(monster)
                    fires.remove(fire)
                    hit = 1
                    break;
            if hit == 1:
                break;

    # Run over all Spaceship Fire and check if the fire hit the  blocks
    for fire in filter(lambda x: x.IsSpaceshipFire == 1, fires):
        hit = 0
        for block in blocks:
            for cell in sorted(block.cells,key = lambda b:b.y,reverse=True):
                if fire.x == cell.x and (fire.y == cell.y or fire.y - 1 == cell.y or fire.y - 2 == cell.y):
                    # if fire hit the block remove the block and the fire
                    block.cells.remove(cell)
                    fires.remove(fire)
                    hit = 1
                    break;
            if hit == 1:
                break;

    # Run over all Monsters Fire and check if the fire hit the Spaceship
    for fire in filter(lambda x: x.IsSpaceshipFire == 0, fires):
        hit = 0
        for cell in sorted(spaceship.cells,key = lambda b:b.y,reverse=False):
            if fire.x == cell.x and (fire.y == cell.y or fire.y + 1 == cell.y or fire.y + 2 == cell.y):
                # if fire hit the Spaceship remove the fire and and red color to the Spaceship
                cell.color = colors.colors["red"]
                fires.remove(fire)
                life += 1
                hit = 1
                break;
        if hit == 1:
            break;


# Redraw Window each iteration
def RedrawWindow():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life, maxLife

    # Fill all surface ar black - "Clear all cells"
    surface.fill(colors.colors["black"])

    # Spaceship Score Text
    SpaceshipLiveText = "Spaceship Live " + str(maxLife - life)

    font = pygame.font.Font('freesansbold.ttf', 16)
    text = font.render(SpaceshipLiveText, True, colors.colors["white"], colors.colors["black"])
    surface.blit(text,  (37, 10))

    # Draw Spaceship
    spaceship.draw()

    # Draw Fire list
    for f in fires:
        f.draw()

    # Draw Monsters list
    for m in monsters:
        m.draw()

    # Draw Blocks list
    for b in blocks:
        b.draw()

    pygame.display.update()


# init all the values to restart game
def restart():
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life
    colors = ColorClass()
    width = 700
    rows = 150
    surface = pygame.display.set_mode((width, width))
    spaceship = SpaceshipClass(int(rows / 2), rows)
    monsters = []
    blocks = []
    fires = []
    life = 0

    CreateMonsters()
    CreateBlocks()

if __name__ == '__main__':
    global colors, surface, width, rows, spaceship, monsters, blocks, fires, life, maxLife
    pygame.init()
    clock = pygame.time.Clock()
    maxLife = 3

    # Init values for new game
    restart()

    # indication of the iteration
    step = 0

    # Monsters step move for Dance
    move = 1
    while True:
        pygame.time.delay(100)
        clock.tick(50)
        step += 1

        # Spaceship move and fire
        SpaceshipMoveAndFire()

        if step % 10 == 0:
            # every 10th iteration 1 Monsters shoot
            MonsterFire()

            # every 40th iteration Monsters change direction
            if step % 40 == 0:
                move *= -1
            MonstersDance(move)

        FireMove()

        # Check fire hits
        Boom()

        # Update the new position for all objects
        RedrawWindow()

        # Check if Spaceship is dead
        if maxLife - life == 0:
            root = tk.Tk()

            # message box to ask for play again or escape
            MsgBox = tk.messagebox.askquestion('Looser', 'Want to try again?',icon='warning')
            if MsgBox == 'yes':
                root.destroy()
                restart()
            else:
                pygame.quit()
                break

        # Check if Spaceship is Kill all the Monsters
        if len(monsters) == 0:
            root = tk.Tk()

            # message box to ask for play again or escape
            MsgBox = tk.messagebox.askquestion('Winner', 'Want to play again?', icon='warning')
            if MsgBox == 'yes':
                root.destroy()
                restart()
            else:
                pygame.quit()
                break




