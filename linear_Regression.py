class linear_Regression:
   
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.m = 10 # slope of the line
        self.b = 40 # y-intercept of the line
        self.predictions = []
        self.error = []

    def predict(self): # predicting the values of y based on the linear equation y = mx + b
        for value in self.x:
            prediction = self.m * value + self.b
            self.predictions.append(prediction)
        return self.predictions

    def calculate_error(self): # cost function or loss function or mean squared error
        for actual, predicted in zip(self.y, self.predictions):
            error = actual - predicted
            self.error.append(error**2)

        mse = sum(self.error) / len(self.error) # mean squared error
        return mse

if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    y = [50, 55, 65, 70, 80]

    model = linear_Regression(x, y)
    predictions = model.predict()
    mse = model.calculate_error()

    print("Predictions:", predictions)
    print("Mean Squared Error:", mse)

    print("prediction for x=6:", model.m * 6 + model.b)