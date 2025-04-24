import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv("data/cardio_train.csv", sep=";")

X = df.drop(columns=["id", "cardio"])
y = df["cardio"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

joblib.dump(model, "app/modelo.pkl")

print("✅ Modelo reentrenado y guardado en 'app/modelo.pkl'")
