from sklearn.tree import DecisionTreeClassifier

# Weather: 0 = Sunny, 1 = Rainy
# Play: 0 = No, 1 = Yes
X = [[0], [0], [1], [1]]
y = [0, 0, 1, 1]

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[1]])
print("Prediction:", "Yes" if prediction[0] == 1 else "No")
