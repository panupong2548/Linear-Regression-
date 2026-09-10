from sklearn.linear_model import LinearRegression
x = [[1], [2], [3], [4], [5]]
y = [50,55,65,70,80]
model = LinearRegression()
model.fit(x, y)
prediction = model.predict([[6]])
print(prediction) 
print("Weight:", model.coef_)
print("Bias:", model.intercept_)