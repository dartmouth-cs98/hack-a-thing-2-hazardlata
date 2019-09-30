class DRL:
    def __init__(self, game):
        self.game = game
        self.reward = 0

    # gets state of game as an array of 11 0s and 1s
    # if snake is immediately in danger (right, left and straight)
    # if snake is moving up, down, left or right
    # if the food is above, below, on the left of or on the right of the snake
    def get_state(self)
        # obstacles
        danger_left = 0
        danger_right = 0
        danger_straight = 0

        head_x, head_y = self.game.snake[0]
        left = (head_x - 1, head_y)
        right = (head_x + 1, head_y)
        straight = (head_x, head_y + self.game.direction)

        if self.game.check_collision(left):
            danger_left = 1
        if self.game.check_collision(right):
            danger_right = 1
        if self.game.check_collision(straight):
            danger_straight = 1

        # which way snake is moving
        move_up = 0
        move_down = 0
        move_right = 0
        move_left = 0

        if self.game.direction == self.game.up:
            move_up = 1
        elif self.game.direction == self.game.down:
            move_down = 1
        elif self.game.direction == self.game.right:
            move_right = 1
        elif self.game.direction == self.game.left:
            move_left = 1

        # where the food is in relation to snake
        food_above = 0
        food_below = 0
        food_right = 0
        food_left = 0

        delta_x = head_x - self.game.food[0]
        delta_y = head_y - self.game.food[1]

        if delta_x > 0:
            food_left = 1
        elif delta_x < 0:
            food_right =  1

        if delta_y > 0:
            food_above = 1
        elif delta_y < 0:
            food_below = 1

        return [danger_left, danger_right, danger_straight, move_up, move_down, move_right, move_left, food_above, food_below, food_right, food_left]
