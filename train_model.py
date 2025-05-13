import pickle
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

# Load your data
df = pd.read_csv('crop_recommendation.csv', encoding = 'latin1')
X = df[['Nitrogen', 'Phosphorous', 'Potassium', 'temperature', 'ph', 'humidity']]
y = df['label']

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the trained model
with open('crop_recommendation_model.pkl', 'wb') as f:
    pickle.dump(model, f)
