"""
Platformer Game
"""
import arcade
from vehicle import Vehicle

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "AI_VEHICLE"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.2
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 2



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.scene = None
        self.player_sprite = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.scene = arcade.Scene()
        image_source = ":resources:images/space_shooter/playerShip1_blue.png"
        self.player_sprite = Vehicle(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.scene.add_sprite("Player", self.player_sprite)

        # for x in range(0, 1250, 64):
        #     wall = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
        #     wall.center_x = x
        #     wall.center_y = 32
        #     self.scene.add_sprite("Walls", wall)

        coordinate_list = [[512, 96], [256, 96], [768, 96]]

        for coordinate in coordinate_list:
            # Add a crate on the ground
            wall = arcade.Sprite(
                ":resources:images/tiles/boxCrate_double.png", TILE_SCALING
            )
            wall.position = coordinate
            self.scene.add_sprite("Walls", wall)


        # Create the 'physics engine'

        self.physics_engine = arcade.PhysicsEngineSimple(

            self.player_sprite, self.scene.get_sprite_list("Walls")

        )


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        # self.player_sprite.slow_down()

        self.scene.draw()


    def on_key_press(self, key, modifiers):
        self.player_sprite.move(key)

        """Called whenever a key is pressed."""






    def on_key_release(self, key, modifiers):
        self.player_sprite.stop_acceleration_in_direction(key)


    def on_update(self, delta_time):

        """Movement and game logic"""


        # print(self.player_sprite)


        self.player_sprite.slow_down()
        # Move the player with the physics engine
        self.physics_engine.update()
        # print(self.player_sprite)



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()