from cs1lib import *
from random import randint

class Snake:
    def __init__(self):
        # graphical components
        self.board_width = 1600
        self.board_height = 1600
        self.snake_block_dimensions = 10

        # game components
        self.width = 20
        self.height = 20
        self.right = (1, 0)
        self.left = (-1, 0)
        self.up = (0, 1)
        self.down = (0, -1)

        # snake components
        self.snake = []                 # array of snake (x, y) coordinates for each block of the snake
        self.direction = (0, 1)         # x, y where (0, 1) is up, (0, -1) is down, (1, 0) is right, and (0, 1) is left
        self.score = 0
        self.food = None

    #### GAME LOGIC ####
    def check_collision(self):
        # get coordinates of snake head
        head = self.snake[0]
        head_x, heady_y = head[0], head[1]

        # checks out-of-bounds snake (no-wrapping around screen)
        if head_x < 0 or head_x > self.width or head_y < 0 or head_y > self.height:
            return True

        # checks self-colliding snake
        for each in self.snake[1:]
            if each = (head_x, head_y):
                return True

        # no collision
        return False

    #### INPUTS ####
    def turn_right(self):
        self.direction = self.right

    def turn_left(self):
        self.direction = self.left

    def turn_up(self):
        self.direction = self.up

    def turn_down(self):
        self.direction = self.down

    #### GRAPHICS ####
    # updates graphics
    def update(self):
        # calculate where new head will be
        new_head_coordinates = self.add_vectors(self.snake[0], self.direction)

        # insert new head_coordinates into beginning of list
        self.snake.insert(0, new_head_coordinates)

        # pop tail
        self.snake.pop()

    # adds vectors for easier snake drawing
    def add_vectors(self, (x1, y1), (x2, y2)):
        return (x1 + x2, y1 + y2)

    # draws the board itself
    def draw_board(self):
        set_fill_color(0, 0, 0)
        draw_rectangle(0, 0, self.board_width, self.board_height)

    # draws everything (wrapped for passing to CS1lib)
    def draw_all(self):
        self.draw_board()

    # displays everything
    def display(self):
        start_graphics(self.draw_all, width=self.board_width, height=self.board_height)

snake = Snake()
snake.display()
