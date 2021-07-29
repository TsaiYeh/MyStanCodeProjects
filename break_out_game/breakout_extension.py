"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

# Constant
FRAME_RATE = 1000 / 120         # 120 frames per second
NUM_LIVES = 3			        # Number of attempts
PROP_Y_SPEED = 5                # Vertical speed of props dropping.


def main():
    """
    :return:
    """
    graphics = BreakoutGraphics()                       # Define graphics as an object produced from BreakoutGraphics.
    graphics.lives = NUM_LIVES                          # Define lives as the number of attempts.

    while graphics.lives > 0:                                               # When user still have lives
        pause(FRAME_RATE)
        if graphics.start:                                                  # When user clicks mouse and start the game
            graphics.ball.move(graphics.get_dx(), graphics.get_dy())        # Let ball move with velocity dx and dy.
            if graphics.collide():                                          # When the ball collides something
                graphics.set_dy(-graphics.get_dy())                         # Let the ball bounces back
            if graphics.prop_on_screen:                                     # When there's a prop on the screen
                graphics.prop.move(0, PROP_Y_SPEED)                         # Let the prop drop
                if graphics.prop.y > graphics.window.height:                # When the prop exits the screen
                    graphics.prop_on_screen = False                         # Turn off the prop switch
                if graphics.catch_prop():                                   # When paddle catches the prop
                    if graphics.prop is graphics.add_lives:
                        graphics.window.remove(graphics.prop)
                        graphics.lives += 1                                 # User's lives plus 1
                        graphics.lives_label.text = 'Lives: ' + str(graphics.lives)         # Update lives_label
                    else:
                        graphics.get_superpower()                           # Enable the power of other kinds of props
                    graphics.prop_on_screen = False                         # Turn off the prop switch

            # When the ball collide the left or right side of the window, the ball bounces back.
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                graphics.set_dx(-graphics.get_dx())

            # When the ball collide the upper side of the window, the ball bounces back.
            if graphics.ball.y <= 0:
                graphics.set_dy(-graphics.get_dy())

            # When the ball falls out of the lower side of the window, the ball will not bounce back.
            if graphics.ball.y >= graphics.window.height:
                graphics.lives -= 1           # user lose one life
                graphics.lives_label.text = 'Lives: ' + str(graphics.lives)
                graphics.start = False        # turn off the switch and ball will start running again when mouse clicks.
                graphics.window.add(graphics.ball, x=(graphics.window.width - graphics.ball.width) / 2,
                                    y=(graphics.window.height - graphics.ball.height) / 2)  # Add a new ball in the original position

            if graphics.count == graphics.total_brick:          # When ball hits and removes all the bricks
                graphics.win()                                  # User wins the game

    graphics.lose()                                             # when user consumes all the lives, he loses the game.


if __name__ == '__main__':
    main()
