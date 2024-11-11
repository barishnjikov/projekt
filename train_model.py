import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Učitavanje podataka
iris = load_iris()
X = iris.data
y = iris.target

# Podjela podataka na skupove za treniranje i testiranje
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treniranje modela
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Spremanje modela
with open('model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model je uspješno generiran i spremljen kao 'model.pkl'.")



