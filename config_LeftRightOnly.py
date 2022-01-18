F_HEIGHT = 20
W_HEIGHT = 2
HEIGHT_MUL = 30
WIDTH_MUL = 40
WIDTH = 10
ACTION_SPACE = [0,1,2]

environ_settings = {
'P_HEIGHT': 2,  # Height of the player
'F_HEIGHT': F_HEIGHT,  # Height of the field
'W_HEIGHT': W_HEIGHT,  # Height of the walls
'WIDTH': WIDTH,  # Width of the field and the walls
'MIN_H_WIDTH': 2,  # Minimum width of the holes
'MAX_H_WIDTH': 6,  # Maximum width of the holes
'MIN_P_WIDTH': 2,  # Minimum Width of the player
'MAX_P_WIDTH': 6,  # Maximum Width of the player
'HEIGHT_MUL': HEIGHT_MUL,  # Height Multiplier (used to draw np.array as blocks in pygame )
'WIDTH_MUL': WIDTH_MUL,  # Width Multiplier (used to draw np.array as blocks in pygame )
'WINDOW_HEIGHT': (F_HEIGHT + 1) * HEIGHT_MUL * 2,  # Height of the pygame window
'WINDOW_WIDTH': (WIDTH) * WIDTH_MUL,  # Widh of the pygame window

'ENVIRONMENT_SHAPE': (F_HEIGHT, WIDTH, 1),
'ACTION_SPACE': ACTION_SPACE,
'ACTION_SPACE_SIZE': len(ACTION_SPACE),
'PUNISHMENT': -500,  # Punishment increment
'REWARD': 10,  # Reward increment
'score': 0,  # Initial Score

'MOVE_WALL_EVERY': 1,  # Every how many frames the wall moves.
'MOVE_PLAYER_EVERY': 1,  # Every how many frames the player moves.
'frames_counter': 0,

'COMPUTER_PLAYER': False,
'PREVIEW_TICK_DEFAULT': 27
}


