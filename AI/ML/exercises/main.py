from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

y = [10, 20, 30, 40, 50,
     60, 70, 80, 90, 100]

model=LinearRegression()

x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model.fit(x_train,y_train)

prediction=model.predict(x_test)

print("predict:",x_test)

print(prediction)