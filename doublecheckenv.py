from dojenv import dojEnv
import numpy as np
import time
import sys

#np.set_printoptions(threshold=sys.maxsize)

env = dojEnv()
episodes = 50
# for i in range(10):
#     print(env.observation_space.sample())


for episode in range(episodes):
    observation = env.reset()
    done = False
    while not done:
        time.sleep(.05)
        action = env.action_space.sample()
        env.render()
        observation, reward, done, info = env.step(action)
        print(np.fliplr(np.rot90(m=observation, k=3)))
        print(reward)
        print(done)
        print(info)
        print("\n")




