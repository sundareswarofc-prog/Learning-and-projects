from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]

y = [20, 30, 40, 50, 60]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[8]])

print(prediction)