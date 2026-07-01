class simpleKNN:
    def __init__(self, k =3 ):
        self.k = k
        self.X_train = []
        self.y_train = []
    def fit(self, X, y):
        self.X_train = X
        self.y_train = y
    def predict(self, unknow_points):
        distances = []
        for i in range(len(self.X_train)):
            current_age = self.X_train[i]
            current_label = self.y_train[i]
            distance_away = abs(current_age - unknow_points)
            distances.append([distance_away, current_label])
        distances.sort()
        zero_votes = 0
        one_votes = 0
        for i in range(self.k):
            neighbour_label = distances[i][1]
            if neighbour_label == 0:
                zero_votes += 1
            else:
                one_votes += 1
            if zero_votes > one_votes:
                return 0
            else:
                return 1

X_train = [5, 10, 15, 65, 70, 80]
y_train = [0,  0,  0,  1,  1,  1]  # Three 0s and Three 1s

knn = simpleKNN(k=3)

# 3. Give it the data
knn.fit(X_train, y_train)

# 4. Give it a mystery test age to predict!
test_age = 10
prediction = knn.predict(test_age)

print("--- KNN TEST RESULT ---")
print(f"For age {test_age}, the model predicts class: {prediction}")
if prediction == 0:
    print("Interpretation: Child/Youth")
else:
    print("Interpretation: Senior Citizen")