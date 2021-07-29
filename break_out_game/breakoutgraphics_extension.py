"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by Sonja Johnson-Yu, Kylie Jue, Nick Bowman, and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel, GPolygon
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

# Constant
BRICK_SPACING = 5           # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40            # Height of a brick (in pixels).
BRICK_HEIGHT = 15           # Height of a brick (in pixels).
BRICK_ROWS = 10             # Number of rows of bricks.
BRICK_COLS = 10             # Number of columns of bricks.
BRICK_OFFSET = 50           # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10            # Radius of the ball (in pixels).
PADDLE_WIDTH = 75           # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15          # Height of the paddle (in pixels).
PADDLE_OFFSET = 50          # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 5         # Initial vertical speed for the ball.
MAX_X_SPEED = 5             # Maximum initial horizontal speed for the ball.
NUM_LIVES = 3			    # Number of attempts


class BreakoutGraphics:
    """
    The class of displaying all graphical objects on a window and define methods
    that can detect ball's movement and interactions with the existing objects.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title='Breakout Game')

        # Create welcome words before starting the game.
        welcome1 = GLabel('Welcome to')
        welcome2 = GLabel('breakout game!')
        welcome1.font = 'Arial-40'
        welcome2.font = 'Arial-40'
        self.window.add(welcome1, 0, 300)
        self.window.add(welcome2, 60, 360)
        pause(1500)
        self.window.remove(welcome1)
        self.window.remove(welcome2)

        # Create a paddle
        self.paddle_width = paddle_width
        self.paddle_height = paddle_height
        self.paddle = GRect(self.paddle_width, self.paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, (self.window.width - self.paddle.width) / 2,
                        (self.window.height - self.paddle.height - paddle_offset))

        # Center a filled ball in the graphical window
        self.ball_radius = ball_radius
        self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, (self.window.width - self.ball.width) / 2,
                        (self.window.height - self.ball.height) / 2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx

        # Draw bricks
        self.brick_x_position = 0
        self.brick_y_position = BRICK_OFFSET
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i < 2:
                    self.brick.fill_color = 'red'
                elif i < 4:
                    self.brick.fill_color = 'orange'
                elif i < 6:
                    self.brick.fill_color = 'yellow'
                elif i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'
                self.window.add(self.brick, self.brick_x_position, self.brick_y_position)
                self.brick_x_position += brick_width + brick_spacing
            self.brick_x_position = 0                                   # back to the left side
            self.brick_y_position += brick_height + brick_spacing       # move to next row

        # Define count when the ball hits a brick. When count equals to the number of bricks, user wins the game.
        self.count = 0                                                  # Initial count is 0.
        self.total_brick = brick_rows * brick_cols                      # Calculate the number of total bricks.

        # Define score which user achieves in the game, showing at the lower-left side of the window.
        self.score = 0                                                  # Initial score is 0.
        self.score_label = GLabel('Score: ' + str(self.score))
        self.score_label.font = 'Arial-24'
        self.window.add(self.score_label, 0, self.window.height)

        # Define lives as the number of attempts user can have for the game.
        self.lives = NUM_LIVES
        self.lives_label = GLabel('Lives: ' + str(self.lives))
        self.lives_label.font = 'Arial-24'
        self.window.add(self.lives_label, self.window.width - self.lives_label.width, self.window.height)

        # Initialize our mouse listeners
        self.start = False                                              # Set a switch to decide if the game starts.
        onmousemoved(self.change_position)
        onmouseclicked(self.start_running)

        # Define the positions of 4 corners of the ball.
        self.corner1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.corner2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.corner3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.corner4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        # Define the image of props which may drop when the ball hits the bricks
        self.long_paddle = GRect(30, 10)                        # long_paddle will make paddle longer
        self.long_paddle.filled = True
        self.long_paddle.fill_color = 'lightsage'
        self.long_paddle.color = 'lightsage'

        self.short_paddle = GRect(10, 30)                       # short_paddle will make paddle shorter
        self.short_paddle.filled = True
        self.short_paddle.fill_color = 'gray'
        self.short_paddle.color = 'gray'

        self.small_ball = GOval(20, 20)                         # small_ball will make ball smaller and harder to catch
        self.small_ball.filled = True
        self.small_ball.fill_color = 'skyblue'
        self.small_ball.color = 'skyblue'

        self.add_lives = GOval(10, 10)                          # add_lives will let user have an extra life
        self.add_lives.filled = True
        self.add_lives.fill_color = 'tomato'
        self.add_lives.color = 'gold'

        self.extra_score = GOval(10, 20)                        # extra_score will let user gets more scores for hits
        self.extra_score.filled = True
        self.extra_score.fill_color = 'forestgreen'
        self.extra_score.color = 'forestgreen'

        self.prop = self.long_paddle
        self.prop_on_screen = False

    def change_position(self, mouse):
        """
        :param mouse: the position of user's mouse.
        :return: When mouse moves, change the position of the paddle.
        """
        self.paddle.x = mouse.x - self.paddle.width / 2               # mouse will be in the middle of paddle at x-axis
        if self.paddle.x < 0:
            self.paddle.x = 0                                         # paddle won't exceed the left side of the window
        if self.paddle.x > self.window.width - self.paddle.width:
            self.paddle.x = self.window.width - self.paddle.width     # paddle won't exceed the right side of the window

    def start_running(self, event):
        """
        :param event: mouse clicks
        :return: When mouse clicks, turn on the switch and the ball starts running.
        """
        self.start = True

    def get_dx(self):
        """
        Getter: get the value of private __dx.
        """
        return self.__dx

    def get_dy(self):
        """
        Getter: get the value of private __dy.
        """
        return self.__dy

    def set_dx(self, new_dx):
        """
        Setter: assign new_dx to the self.__dx.
        :param new_dx: a new velocity of x-direction.
        """
        self.__dx = new_dx

    def set_dy(self, new_dy):
        """
        Setter: assign new_dy to the self.__dy.
        :param new_dy: a new velocity of y-direction
        """
        self.__dy = new_dy

    def collide(self):
        """
        Detect if the ball collide with something by get_object_at its 4 corners' positions.
        If colliding, check it's paddle or brick or others. If it's paddle, return True.
        If it's brick, add one count, update score, remove the brick, drop the props, and then return True.
        If it's other object, return False so ball won't bounce back.
        """
        self.corner1 = self.window.get_object_at(self.ball.x, self.ball.y)
        self.corner2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        self.corner3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.height)
        self.corner4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.height)

        if self.corner1 is not None:
            if self.corner1 is self.paddle:                                             # if the ball hits the paddle
                if self.__dy > 0:
                    return True
            elif (self.corner1 is self.score_label) or (self.corner1 is self.prop) or (self.corner1 is self.lives_label):
                return False
            else:                                                                       # if the ball hits a brick
                self.count += 1                                                         # count plus 1
                self.score += 1                                                         # get one point of the score
                self.score_label.text = 'Score: ' + str(self.score)                     # score wording update
                self.window.remove(self.corner1)                                        # remove the brick
                self.props_appear()                                                     # may drop prop from the brick
                return True

        elif self.corner2 is not None:
            if self.corner2 is self.paddle:
                if self.__dy > 0:
                    return True
            elif (self.corner2 is self.score_label) or (self.corner2 is self.prop) or (self.corner2 is self.lives_label):
                return False
            else:
                self.count += 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)
                self.window.remove(self.corner2)
                self.props_appear()
                return True

        elif self.corner3 is not None:
            if self.corner3 is self.paddle:
                if self.__dy > 0:
                    return True
            elif (self.corner3 is self.score_label) or (self.corner3 is self.prop) or (self.corner3 is self.lives_label):
                return False
            else:
                self.count += 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)
                self.window.remove(self.corner3)
                self.props_appear()
                return True

        elif self.corner4 is not None:
            if self.corner4 is self.paddle:
                if self.__dy > 0:
                    return True
            elif (self.corner4 is self.score_label) or (self.corner4 is self.prop) or (self.corner4 is self.lives_label):
                return False
            else:
                self.count += 1
                self.score += 1
                self.score_label.text = 'Score: ' + str(self.score)
                self.window.remove(self.corner4)
                self.props_appear()
                return True

    def props_appear(self):
        """
        :return: When the ball collides the bricks, there's a percentage that a prop will drop out from the brick.
        """
        if not self.prop_on_screen:
            drop_rate = random.random()                         # Define drop rate as a random float number from 0 to 1

            if drop_rate <= 0.1:
                self.prop = self.long_paddle                    # 10% probability long_paddle will appear.
                self.window.add(self.long_paddle, self.ball.x + BALL_RADIUS, self.ball.y + BALL_RADIUS)
                self.prop_on_screen = True

            elif 0.1 < drop_rate <= 0.2:
                self.prop = self.short_paddle                   # 10% probability short_paddle will appear.
                self.window.add(self.short_paddle, self.ball.x + BALL_RADIUS, self.ball.y + BALL_RADIUS)
                self.prop_on_screen = True

            elif 0.2 < drop_rate <= 0.3:
                self.prop = self.small_ball                     # 10% probability small_ball will appear.
                self.window.add(self.small_ball, self.ball.x + BALL_RADIUS, self.ball.y + BALL_RADIUS)
                self.prop_on_screen = True

            elif 0.3 < drop_rate <= 0.4:
                self.prop = self.add_lives                      # 10% probability add_lives will appear.
                self.window.add(self.add_lives, self.ball.x + BALL_RADIUS, self.ball.y + BALL_RADIUS)
                self.prop_on_screen = True

            elif 0.4 < drop_rate <= 0.5:
                self.prop = self.extra_score                    # 10% probability extra_score will appear.
                self.window.add(self.extra_score, self.ball.x + BALL_RADIUS, self.ball.y + BALL_RADIUS)
                self.prop_on_screen = True

    def catch_prop(self):
        """
        :return: If paddle catches the prop (meaning prop's position is inside paddle), return True.
        """
        if self.paddle.y <= self.prop.y + self.prop.height <= self.paddle.y + self.paddle.height:
            if self.paddle.x <= (self.prop.x + self.prop.width / 2) <= self.paddle.x + self.paddle.width:
                return True

    def get_superpower(self):
        """
        :return: Each prop has different superpower. When paddle catches the prop, prop will release its power.
        long_paddle can make paddle's width longer to catch the ball easier.
        short_paddle can make paddle's width shorter so it'll be more difficult to catch the ball.
        small_ball can make the ball smaller so it'll be more difficult to catch the ball.
        add_lives can let user have an extra life.
        extra_score can let user extra 10 points to have higher scores.
        """
        if self.prop is self.long_paddle:
            self.window.remove(self.prop)
            current_x = self.paddle.x
            current_y = self.paddle.y
            self.window.remove(self.paddle)
            if self.paddle_width <= self.window.width * 0.75:
                self.paddle_width += 30
            self.paddle = GRect(self.paddle_width, self.paddle_height)
            self.paddle.filled = True
            self.window.add(self.paddle, current_x, current_y)

        elif self.prop is self.short_paddle:
            self.window.remove(self.prop)
            current_x = self.paddle.x
            current_y = self.paddle.y
            self.window.remove(self.paddle)
            if self.paddle_width >= 45:
                self.paddle_width -= 30
            self.paddle = GRect(self.paddle_width, self.paddle_height)
            self.paddle.filled = True
            self.window.add(self.paddle, current_x, current_y)

        elif self.prop is self.small_ball:
            self.window.remove(self.prop)
            current_x = self.ball.x
            current_y = self.ball.y
            self.window.remove(self.ball)
            if self.ball_radius > 5:
                self.ball_radius -= 3
            self.ball = GOval(self.ball_radius * 2, self.ball_radius * 2)
            self.ball.filled = True
            self.window.add(self.ball, current_x, current_y)

        elif self.prop is self.extra_score:
            self.window.remove(self.prop)
            self.score += 10
            self.score_label.text = 'Score: ' + str(self.score)

    def lose(self):
        """
        :return: Show 'you lose' when the number of lives becomes 0.
        """
        bg = GRect(self.window_width, self.window_height)
        bg.filled = 'True'
        bg.fill_color = 'darkgrey'
        self.window.add(bg)

        you_lose = GLabel('Sorry, you lose!', x=40, y=300)
        you_lose.font = 'Arial-40'
        you_lose.color = 'white'
        self.window.add(you_lose)

    def win(self):
        """
        :return: Show 'you win' when the user clears all the bricks and still have lives.
        """
        you_win1 = GLabel('Congrats!', x=100, y=300)
        you_win2 = GLabel('You win!', x=120, y=400)
        you_win1.font = 'Arial-40'
        you_win2.font = 'Arial-40'
        self.window.remove(self.ball)
        self.window.add(you_win1)
        self.window.add(you_win2)
