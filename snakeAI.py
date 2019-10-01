# based on code from https://github.com/maurock/snake-ga/blob/master/DQN.py
from keras.optimizers import Adam
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
# from keras.layers import Dense, Dropout
import random
import numpy as np
import pandas as pd
from operator import add

class SnakeAgent(object):

    def __init__(self):
        self.reward = 0
        self.gamma = 0.9
        self.dataframe = pd.DataFrame()
        self.short_memory = np.array([])
        self.agent_target = 1
        self.agent_predict = 0
        self.learning_rate = 0.0005
        self.model = self.network()
        #self.model = self.network("weights.hdf5")
        self.epsilon = 0
        self.actual = []
        self.memory = []

    def add_vectors(self, v1, v2):
        x1, y1 = v1
        x2, y2 = v2
        return (x1 + x2, y1 + y2)

    def get_state(self, game):
        head = game.snake[0]
        head_x, head_y = head

        options = {
            (-1, 0): ((0, -1), (-1, 0), (0, 1)),
            (1, 0): ((0, 1), (1, 0), (0, -1)),
            (0, -1): ((1, 0), (0, -1), (-1, 0)),
            (0, 1): ((-1, 0), (0, 1), (1, 0)),
        }

        left, right, straight = options[game.direction]
        left = (head_x + left[0], head_y + left[1])
        right = (head_x + right[0], head_y + right[1])
        straight = (head_x + straight[0], head_y + straight[1])

        state = [
            game.check_collision(left),
            game.check_collision(right),
            game.check_collision(straight),

            game.direction == game.left,  # moving left
            game.direction == game.right,  # moving right
            game.direction == game.up,  # moving up
            game.direction == game.down,  # moving down


            game.food[0] < head_x,  # food left
            game.food[0] > head_x,  # food right
            game.food[1] > head_y,  # food up
            game.food[1] < head_y  # food down
            ]

        for i in range(len(state)):
            if state[i]:
                state[i]=1
            else:
                state[i]=0

        return np.asarray(state)

    def set_reward(self, game):
        self.reward = 0
        if game.end:
            self.reward = -10
        if game.snake_ate():
            self.reward = 10
        return self.reward

    def network(self, weights=None):
        model = Sequential()
        model.add(Dense(output_dim=120, activation='relu', input_dim=11))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=120, activation='relu'))
        model.add(Dropout(0.15))
        model.add(Dense(output_dim=4, activation='softmax'))
        opt = Adam(self.learning_rate)
        model.compile(loss='mse', optimizer=opt)

        if weights:
            model.load_weights(weights)
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def replay_new(self, memory):
        if len(memory) > 1000:
            minibatch = random.sample(memory, 1000)
        else:
            minibatch = memory
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = reward + self.gamma * np.amax(self.model.predict(np.array([next_state]))[0])
            target_f = self.model.predict(np.array([state]))
            target_f[0][np.argmax(action)] = target
            self.model.fit(np.array([state]), target_f, epochs=1, verbose=0)

    def train_short_memory(self, state, action, reward, next_state, done):
        target = reward
        if not done:
            target = reward + self.gamma * np.amax(self.model.predict(next_state.reshape((1, 11)))[0])
        target_f = self.model.predict(state.reshape((1, 11)))
        target_f[0][np.argmax(action)] = target
        self.model.fit(state.reshape((1, 11)), target_f, epochs=1, verbose=0)
