from cs1lib import *
from random import randint
from time import sleep

class Snake:
    def __init__(self, width, height, p_width, p_height):
        # game components
        self.width = width
        self.height = height
        self.right = (1, 0)
        self.left = (-1, 0)
        self.up = (0, -1)
        self.down = (0, 1)
        self.max_food_tries = 100
        self.start = False
        self.end = False

        # graphical components
        self.board_width = p_width
        self.board_height = p_height
        self.snake_block_dimensions = p_width / width

        # snake components
        self.snake = [self.generate_random_coordinate()]                                # array of snake (x, y) coordinates for each block of the snake
        self.direction = None                                                       # x, y where (0, 1) is up, (0, -1) is down, (1, 0) is right, and (0, 1) is left
        self.score = 0
        self.food = self.spawn_new_food()

    #### GAME LOGIC ####
    # checks for collisions
    def check_collision(self):
        # get coordinates of snake head
        head_x, head_y = self.snake[0]

        # checks out-of-bounds snake (no-wrapping around screen)
        if head_x < -1 or head_x >= self.width or head_y < -1 or head_y >= self.height:
            return True

        # checks self-colliding snake
        for each in self.snake[1:]:
            if each == (head_x, head_y):
                return True

        # no collision
        return False

    # generates random location for food
    def generate_random_coordinate(self):
        rand_x = randint(0, self.width - 1)
        rand_y = randint(0, self.height - 1)

        return (rand_x, rand_y)

    # checks if food is on snake
    def food_on_snake(self, food_x, food_y):
        for each in self.snake:
            if (food_x, food_y) == each:        # loop and check collisions
                return True

        return False

    # spawns new food, not on snake
    def spawn_new_food(self):
        # generates until a food location not on the snake is found (within reason)
        for i in range(self.max_food_tries):
            food_x, food_y = self.generate_random_coordinate()

            if not self.food_on_snake(food_x, food_y):
                return (food_x, food_y)

    # determines if snake has eaten food
    def snake_ate(self):
        return self.snake[0] == self.food

    # updates snake
    def update(self):
        # if the snake ate, elongate him/her and spawn new food
        if self.snake_ate():
            self.score += 1
            self.snake.insert(0, self.food)
            self.food = self.spawn_new_food()
        # if not, just move the snake around
        else:
            # calculate where new head will be
            new_head_coordinates = self.add_vectors(self.snake[0], self.direction)

            # insert new head_coordinates into beginning of list
            self.snake.insert(0, new_head_coordinates)

            # pop tail
            self.snake.pop()

            if self.check_collision():
                print("Collision")
                print(self.snake[0])

                set_clear_color(1, 1, 1)
                clear()
                set_stroke_color(0, 0, 0)
                set_font_size(100)
                draw_text(str(self.score), self.board_width // 2, self.board_height // 2)
                self.start = False
                self.end = True

    #### USER INPUT FOR TESTING ####
    def pressed(self, key):
        self.start = True
        if key == "a":
            self.turn_left()
        elif key == "d":
            self.turn_right()
        elif key == "s":
            self.turn_down()
        elif key == "w":
            self.turn_up()

    #### INPUTS ####
    def turn_right(self):
        if self.direction != self.left:
            print("Turning right")
            self.direction = self.right

    def turn_left(self):
        if self.direction != self.right:
            print("Turning left")
            self.direction = self.left

    def turn_up(self):
        if self.direction != self.down:
            print("Turning up")
            self.direction = self.up

    def turn_down(self):        # for what
        if self.direction != self.up:
            print("Turning down")
            self.direction = self.down

    #### GRAPHICS ####
    # adds vectors for easier snake drawing
    def add_vectors(self, v1, v2):
        x1, y1 = v1
        x2, y2 = v2
        return (x1 + x2, y1 + y2)

    # draws the food
    def draw_food(self):
        set_fill_color(1, 1, 0)
        self.draw_block(self.food)

    # draws a block (either snake or food)
    def draw_block(self, coord):
        # get graphical coordinates
        graphics_x, graphics_y = coord
        graphics_x *= self.snake_block_dimensions
        graphics_y *= self.snake_block_dimensions

        # draw the block
        draw_rectangle(graphics_x, graphics_y, self.snake_block_dimensions, self.snake_block_dimensions)

    # draws the snake itself
    def draw_snake(self):
        # draw head in red
        set_fill_color(1, 0, 0)
        self.draw_block(self.snake[0])

        # draw body in green
        set_fill_color(0, 1, 0)
        for each in self.snake[1:]:
            self.draw_block(each)

    # draws everything (wrapped for passing to CS1lib)
    def play(self):
        if not self.end:
            set_clear_color(0, 0, 0)
            clear()

            # TODO - draw food first then snake so snake is always over food
            self.draw_food()
            self.draw_snake()

            # only updates once game is ready to be played
            if self.start:
                self.update()

    # displays everything
    def display(self):
        start_graphics(self.play, framerate=10, width=self.board_width, height=self.board_height, key_press=self.pressed)

snake = Snake(20, 20, 2000, 2000)
snake.display()
