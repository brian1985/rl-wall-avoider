See original project that this was based off of for learning purposes here: 

https://github.com/ModMaamari/reinforcement-learning-using-python


Additional changes include:

Adjusted the code to work with TF 2.7 (up from 2.3 probably)

Added the ability to move and resize on the same step (4 additional actions - currently building a working model)

Changed reward system slightly to penalize End game fail more harshly. Added penalizing term to reward for extra movements (reducing wiggle of person during intermediate steps).

Changed model structure to include additional CNN layers, and added kernal regularizers to handle the larger model. (Currently under validation - want to see if regularizers can improve performance and/or speed of training.)

Added a fully trained model a computer can use to play the game with (see computerPlayer_Test.py and use the LeftRight config.) that performs without issue at least to a score of 1600 but likely forever (LEFTRIGHT actions only). 

Added the ability to load an existing model (developer in charge of assuring achitecture matches) and use its' weights for pretraining so you can pick up where left off if desired. To do so, manually copy the model name + path into the DQNAgent.load_pretrained_model and set use_pretrained to True in the agent intantiation.

Added config files for use with multiple styles of training and progression. For instance the LeftrightOnly config trains a model with only actions for Left rigth (no resize of person width). Further development with add additional config files for other changes such as resize + move in a single action, new Environment size to accomodate a larger board making it harder to get places. 

<b>Future adds</b>:
<li>I would like to add option for two holes to appear: test using a single hole model (to see if it can handle that change natively), and train a new model to see if the learning can pick up that the best option is the closest hole to its current location.</li>

<li>Add random blocks periodically that would force a player to go around them</li>

<li> Add bonus items as colored blocks that add bonus points. Since color isn't part of the CNN model (it assumes a single dimension on that shape element), the model would need changing.</li>

