import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from how_diverse import dataset1  # Assuming you have the dataset1 available

# Create a copy of the dataset to avoid SettingWithCopyWarning
df_selected = dataset1.copy()

# Encode categorical variables if needed
label_encoder = LabelEncoder()
df_selected['Sex'] = label_encoder.fit_transform(df_selected['Sex'])
df_selected['RaceDesc'] = label_encoder.fit_transform(df_selected['RaceDesc'])
df_selected['PerformanceScore'] = label_encoder.fit_transform(df_selected['PerformanceScore'])

# Define features and target variable
features = ['EmpSatisfaction', 'PerformanceScore', 'EngagementSurvey']
target = 'Termd'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_selected[features], df_selected[target], test_size=0.2, random_state=42)

# Standardize the input features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize the neural network model
model = keras.Sequential([
    layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    layers.Dense(32, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=0)

# Make predictions on the testing set
y_pred_probs = model.predict(X_test)
y_pred = (y_pred_probs > 0.5).astype(int)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

# Print results
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_report}')