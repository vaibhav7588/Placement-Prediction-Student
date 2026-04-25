import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

# 🔹 Load dataset
data = pd.read_csv("placement.csv")

# 🔹 Features (must match app.py EXACTLY)
X = data[['cgpa','ssc','hsc','internships','projects','aptitude','communication','training']]
y = data['placed']

# 🔹 Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔹 Test model
y_pred = model.predict(X_test)

# 🔹 Accuracy
acc = accuracy_score(y_test, y_pred)
print("✅ Accuracy:", round(acc * 100, 2), "%")

# 🔹 Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("📊 Confusion Matrix:")
print(cm)

# 🔹 Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("📁 model.pkl created successfully")
