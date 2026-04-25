import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle

# 🔹 Load dataset
data = pd.read_csv("placement.csv")

# 🔹 Features
X = data[['cgpa','ssc','hsc','internships','projects','aptitude','communication','training']]
y = data['placed']

# 🔹 Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔹 Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 🔹 Prediction
y_pred = model.predict(X_test)

# 🔹 Accuracy
acc = accuracy_score(y_test, y_pred)
print("\n✅ Accuracy:", round(acc * 100, 2), "%")

# 🔹 Confusion Matrix (values)
cm = confusion_matrix(y_test, y_pred)

print("\n📊 Confusion Matrix:")
print("TN:", cm[0][0], " FP:", cm[0][1])
print("FN:", cm[1][0], " TP:", cm[1][1])

# 🔹 Graph display
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot()
plt.title("Confusion Matrix - Placement Prediction")
plt.show()

# 🔹 Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("\n📁 model.pkl created successfully")
