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
CHARACTER_SCALING = 0.4
TILE_SCALING = 0.5

PLAYER_MOVEMENT_SPEED = 2



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        self.scene = None
        self.vehicle = None
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        self.scene = arcade.Scene()
        image_source = ":resources:images/space_shooter/playerShip1_blue.png"
        self.vehicle = Vehicle(image_source, CHARACTER_SCALING)
        self.vehicle.center_x = 64
        self.vehicle.center_y = 128
        self.scene.add_sprite("Vehicle", self.vehicle)

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

            self.vehicle, self.scene.get_sprite_list("Walls")

        )


    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        # self.vehicle.slow_down()

        self.scene.draw()


    def on_key_press(self, key, modifiers):
        self.vehicle.move(key)

        """Called whenever a key is pressed."""






    def on_key_release(self, key, modifiers):
        self.vehicle.stop_acceleration_in_direction(key)


    def on_update(self, delta_time):

        """Movement and game logic"""

        self.vehicle.slow_down()
        # Move the player with the physics engine
        self.physics_engine.update()



def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()