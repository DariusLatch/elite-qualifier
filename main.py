
import pygame  # load pygame keywords

"""
Objects
"""


class Player(pygame.sprite.Sprite):
    """
    Spawn a player
    """

    def __init__(self):
        super().__init__()
        self.movex = 0  # move along X
        self.movey = 0  # move along Y
        self.health = 10

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(RED)

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()

    def control(self, x, y):
        """
        control player movement
        """
        self.movex += x
        self.movey += y

    def update(self):
        """
        Update sprite position
        """
        self.rect.x += self.movex
        self.rect.y += self.movey

        enemy_hit_list = pygame.sprite.spritecollide(self, enemy_list, False)
        for enemy in enemy_hit_list:
            self.health -= 1
            print(self.health)

    def gravity(self):
        if self.rect.y > worldy and self.movey >= 0:
            self.movey = 0
            self.rect.y = worldy - self.height
        else:
            self.movey += 3  # How fast the player falls

class Enemy(pygame.sprite.Sprite):
    """
    Spawn an enemy
    """

    def __init__(self, x, y):
        super().__init__()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.width = 40
        self.height = 60
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(BLUE)

        self.movey = 0

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.counter = 0  # counter variable

    def move(self):
        """
        enemy movement
        """
        distance = 80
        speed = 8

        if 0 <= self.counter <= distance:
            self.rect.x += speed
        elif distance <= self.counter <= distance * 2:
            self.rect.x -= speed
        else:
            self.counter = 0

        self.counter += 1

        self.rect.y += self.movey
        
        if self.rect.y > worldy and self.movey > 0:
            self.movey = 0
            self.rect.y = worldy - self.height
        else:
            self.movey += 3


class Level():
    @staticmethod
    def bad(lvl, enemy_location):
        if lvl == 1:
            enemy = Enemy(enemy_location[0], enemy_location[1])  # spawn enemy
            enemy_list = pygame.sprite.Group()  # create enemy group
            enemy_list.add(enemy)              # add enemy to group
        if lvl == 2:
            enemy_list = None
            print(f"Level {lvl}")

        return enemy_list

    @staticmethod
    def ground(lvl, x, y, width, height):
        ground_list = pygame.sprite.Group()
        if lvl == 1:
            ground = Platform(x, y, width, height, GREEN)
            ground_list.add(ground)

        if lvl == 2:
            ground_list = None
            print(f"Level {lvl}" )

        return ground_list

    @staticmethod
    def platform(lvl):
        plat_list = pygame.sprite.Group()
        if lvl == 1:
            plat = Platform(200, worldy - 25 - 128, 285, 67, WHITE)
            plat_list.add(plat)
            plat = Platform(500, worldy - 25 - 320, 197, 54, WHITE)
            plat_list.add(plat)
        if lvl == 2:
            plat_list = None
            print(f"Level {lvl}" )

        return plat_list


class Platform(pygame.sprite.Sprite):
    # x location, y location, img width, img height, img file
    def __init__(self, x, y, width, height, color):
        super().__init__()

        # Make a platform, of the size and color specified in the parameters
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x

"""
Setup
"""

pygame.display.set_mode()
worldx = 800
worldy = 600
fps = 40  # frame rate
ani = 4   # animation cycles
clock = pygame.time.Clock()
pygame.init()
world = pygame.display.set_mode([worldx, worldy])
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
main = True

player = Player()   # spawn player
player.rect.x = 0   # go to x
player.rect.y = 0   # go to y
player_list = pygame.sprite.Group()
player_list.add(player)
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10  # how many pixels to move

enemy_location = [200, 20]
enemy_list = Level.bad(1, enemy_location)
ground_list = Level.ground(1, 0, worldy-25, 1080, 100)
plat_list = Level.platform(1)

"""
Main Loop
"""

while main:
    world.fill(BLACK)
    player.gravity()
    player.update()  # update player position
    player_list.draw(world)  # draw player
    enemy_list.draw(world)  # refresh enemies
    ground_list.draw(world)
    plat_list.draw(world)
    for e in enemy_list:
        e.move()
    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(-steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(steps, 0)
            if event.key == pygame.K_UP or event.key == ord('w'):
                print('jump')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                player.control(steps, 0)
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                player.control(-steps, 0)
            if event.key == ord('q'):
                pygame.quit()
                main = False
