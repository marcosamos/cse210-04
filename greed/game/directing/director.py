import random
from game.shared.color import Color
from game.shared.point import Point
from game.shared.velocity import Velocity
from game.casting.rock import Rock
from game.casting.gem import Gem

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the player.
        
        Args:
            cast (Cast): The cast of actors.
        """
        player = cast.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the players position and resolves any collisions with rocks or gems.
        
        Args:
            cast (Cast): The cast of actors.
        """
       
        score = cast.get_first_actor("score")
        player = cast.get_first_actor("player")
        rocks = cast.get_actors("rocks")
        gems = cast.get_actors("gems")

        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
        for rock in rocks:
            if player.get_position().equals(rock.get_position()):
                player.rock_points() 
                score.set_text(f"Score: {player.get_score()}")   
                cast.remove_actor("rocks", rock) 

            rock.move_next(max_x, max_y)  
          

        for gem in gems:
            if player.get_position().equals(gem.get_position()):
                player.gem_points()   
                score.set_text(f"Score: {player.get_score()}")    
                cast.remove_actor("gems", gem) 
            gem.move_next(max_x, max_y)  
         
        
        if len(gems) > 0:
            score.set_text(f"You have collected  {player.get_score()} gems! Well done! Close window to end game.")    

    def create_rocks(self, cast):
        x = random.randint(1, 60 - 1)
        y = random.randint(1, 40 - 1)
        position = Point(x, y)
        position = position.scale(15)
        speed = Velocity(0, 1)

        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = Color(r, g, b)
        
        rock = Rock()
        rock.set_text("O")
        rock.set_font_size(15)
        rock.set_color(color)
        rock.set_position(position)
        rock.set_velocity(speed)
        cast.add_actor("rocks", rock)

    def create_gems(self, cast):
        x = random.randint(1, 60 - 1)
        y = random.randint(1, 40 - 1)
        position = Point(x, y)
        position = position.scale(15)
        speed = Velocity(0, 1)

        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = Color(r, g, b)
        
        gem = Gem()
        gem.set_text("*")
        gem.set_font_size(15)
        gem.set_color(color)
        gem.set_position(position)
        gem.set_velocity(speed)
        cast.add_actor("gems", gem)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
