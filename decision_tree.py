
from sklearn.tree import DecisionTreeClassifier

X = [
    [2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80],
    [7, 85],
    [8, 90],
    [9, 95]
]

y = [
    "Fail", "Fail", "Fail", "Pass",
    "Pass", "Pass", "Pass", "Pass"
]

model = DecisionTreeClassifier(random_state=0)
model.fit(X, y)

hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))

prediction = model.predict([[hours, attendance]])

print("Predicted Result:", prediction[0])
