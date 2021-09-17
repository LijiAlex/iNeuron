class Perceptron:
  def __init__(self,eta,epochs):
    self.weights = np.random.randn(3) *1e-4 #small weight initialization
    print(f"initial weights before training: {self.weights}")
    self.eta = eta #learning rate
    self.epochs = epochs #no of epochs
  
  def activationFunction(self,inputs,weights):
    z = np.dot(inputs, weights) # z = X * W  
    return np.where(z > 0, 1, 0) # if >0 return 1 else 0

  def fit(self,X,y):  #training
    self.X = X
    self.y = y

    x_with_bias = np.c_[X, -np.ones((len(X),1))] #len is no of rows of X np.c_ is concatinaete
    print(f"X with bias: \n{x_with_bias}")

    for epoch in range(self.epochs):
      print("__"*10)
      print(f"for epoch:{epoch}")
      print("__"*10)

      y_hat = self.activationFunction(x_with_bias,self.weights) #forward propagation
      print(f"predicted value after forward pass: \n{y_hat}")
      self.error = self.y - y_hat
      print(f"error: \n{self.error}")
      self.weights = self.weights + self.eta * np.dot(x_with_bias.T,self.error) #backward propagation
      print(f"corrected weights after epoch:{epoch}/{self.epochs} :{self.weights} ")
      print("#####"*10)
      
  def predict(self,X):
    x_with_bias = np.c_[X, -np.ones((len(X), 1))]
    return self.activationFunction(x_with_bias,self.weights)

  def total_loss(self):
    total_loss = np.sum(self.error)
    print(f"total loss : {total_loss}")
    return total_loss