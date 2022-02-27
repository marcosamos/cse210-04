import random
from game.casting.actor import Actor
from game.casting.rock import Rock
from game.casting.gem import Gem
from game.casting.player import Player
from game.casting.cast import Cast
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.shared.velocity import Velocity


FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
START_ROCKS = 20
START_GEMS = 20
START_TNTS= 5
START_EMERALDS = 10
START_RUBIES = 5
START_DIAMONDS = 2
START_CAVES = 2

def main():
    
    # create the cast
    cast = Cast()
    
    # create the score
    score = Actor()
    score.set_text("Score: 0")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    score.set_velocity(Velocity(0,0))
    cast.add_actor("score", score)
      
    # create the player
    x = int(MAX_X / 2)
    y = MAX_Y - 25
    position = Point(x, y)
    speed = Velocity(0,0)

    player = Player()
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)
    player.set_position(position)
    player.set_velocity(speed)
    cast.add_actor("player", player)
    
    for n in range(START_ROCKS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        speed = Velocity(0, 1)

        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text("0")
        rock.set_font_size(FONT_SIZE)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_velocity(speed)
        cast.add_actor("rocks", rock)
    
    
    for n in range(START_GEMS):
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)
        speed = Velocity(0, 1)

        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_velocity(speed)
        cast.add_actor("gems", gem)
    
    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()