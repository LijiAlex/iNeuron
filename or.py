from utils.model import Perceptron
from utils.all_utils import *

OR = {
    "x1": [0,0,1,1],
    "x2": [0,1,0,1],
    "y": [0, 1, 1, 1]
}

df_OR = pd.DataFrame(OR)

X,y = prepare_data(df_OR)
print(X)
print(y)

ETA = 0.3 # learning rate between 0 and 1 (assume)
EPOCHS = 10

model_OR = Perceptron(eta=ETA, epochs=EPOCHS)

model_OR.fit(X, y)

_ = model_OR.total_loss()

model_OR.predict(X)