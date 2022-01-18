import time
import pygame
import numpy as np
from time import sleep
from keras.models import load_model

from Train_GridSearch import Environment
from config_LeftRightOnly import environ_settings as settings

model_name_ = "M0_32C_16C_32D_32D_ECC2_1A-5Ac_LeftRightModel.model"
model = load_model(f'SavedModels/{model_name_}')



# EX : say you have the model in a folder called "models" and model's name is "myModel.model"
# model_name_ = "myModel.model"
# model = load_model(f'models/{model_name_}')


# Now We can use the trained agent to play the game :
# Next code initializes the environment and the agent
# then uses the trained agent to play 20 rounds of the game and
# records the score and time of each round
env2 = Environment()
# env2.WALL_SPEED = 1
env2.MOVE_WALL_EVERY = settings['MOVE_WALL_EVERY']

start = time.time()
for _ in range(1):
    WINDOW          = pygame.display.set_mode((env2.WINDOW_WIDTH, env2.WINDOW_HEIGHT))
    clock           = pygame.time.Clock()
    score_increased = False
    game_over       = False
    _ = env2.reset()
    env2.COMPUTER_PLAYER = True
    pygame.display.set_caption("Game")
    while not game_over:
        clock.tick(settings['PREVIEW_TICK_DEFAULT'])
        prd = model.predict((env2.field.body/env2.MAX_VAL).reshape(-1, *env2.ENVIRONMENT_SHAPE))

        actions = np.argmax(prd[0])
        print("actions:", actions)
        _,reward, game_over \
            = env2.step(actions)
        env2.render(WINDOW = WINDOW)


    #####################################################
    a = int(time.time()-start)
    print(f"Score {env2.score} in {a//60}:{a%60}")
    sleep(0.5)
    WINDOW.fill(env2.WHITE)
    env2.print_text(WINDOW = WINDOW, text_cords = (env2.WINDOW_WIDTH // 2, env2.WINDOW_HEIGHT// 2),
                       text = f"Game Over - Score : {env2.score}", color = env2.RED, center = True)
    pygame.display.update()
    sleep(0.1)
pygame.quit()
