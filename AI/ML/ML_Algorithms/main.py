# 1: Linear Regression -------------------

from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]
y = [20, 30, 40, 50, 60]

model = LinearRegression()

model.fit(X, y)

result = model.predict([[6]])

print(result)

# How does it work?

# It learns a mathematical relationship between input and output.

# For a simple linear relationship:

# ----------------------------------------------------------------------------------------------------


# 2: Logistic Regression -------------------

from sklearn.linear_model import LogisticRegression

X = [[1], [2], [3], [4], [5], [6]]
y = [0, 0, 0, 1, 1, 1]

model = LogisticRegression()

model.fit(X, y)

result = model.predict([[5]])

print(result)

# Here:
# - 0 = Fail.
# - 1 = Pass.
# The model learns to classify the student based on study hours.


# ----------------------------------------------------------------------------------------------------


# 3: Decision Tree ---------------------

from sklearn.tree import DecisionTreeClassifier

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = DecisionTreeClassifier()

model.fit(X, y)

print(model.predict([[4]]))

# Decision Trees can be used for both classification and regression.


# ----------------------------------------------------------------------------------------------------



# 4: Random Forest  -------------------------

from sklearn.ensemble import RandomForestClassifier

X = [[1], [2], [3], [4], [5]]
y = [0, 0, 1, 1, 1]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

print(model.predict([[4]]))


# Here:
# - n_estimators=100 means the forest contains 100 decision trees.
# - random_state=42 makes the randomized training reproducible.


# ----------------------------------------------------------------------------------------------------


# 5: K-Means Clustering -------------------------


from sklearn.cluster import KMeans

X = [
    [10], [12], [15],
    [80], [85], [90],
    [40], [45], [50]
]

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X)

print(model.labels_)


# - n_clusters=3 means we want three groups.
# - fit() discovers the groups.
# - labels_ tells us which group each data point belongs to.
# The group numbers themselves do not have a fixed business meaning.