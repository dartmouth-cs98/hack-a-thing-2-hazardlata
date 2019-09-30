class DRL:
    def __init__(self):
        self.reward = 0

    # gets state of game as an array of 11 0s and 1s
    # if snake is immediately in danger (right, left and straight)
    # if snake is moving up, down, left or right
    # if the food is above, below, on the left of or on the right of the snake
    def get_state(self, game)
        # obstacles
        danger_left = 0
        danger_right = 0
        danger_straight = 0

        # which way snake is moving
        move_up = 0
        move_down = 0
        move_right = 0
        move_left = 0

        if game.direction == game.up:
            move_up = 1
        elif game.direction == game.down:
            move_down = 1
        elif game.direction == game.right:
            move_right = 1
        elif game.direction == game.left:
            move_left = 1

        # where the food is in relation to snake
        food_above = 0
        food_below = 0
        food_right = 0
        food_left = 0

        delta_x = game.snake[0][0] - game.food[0]
        delta_y = game.snake[0][1] - game.food[1]

        if delta_x > 0:
            food_left = 1
        elif delta_x < 0:
            food_right =  1

        if delta_y > 0:
            food_above = 1
        elif delta_y < 0:
            food_below = 1
