import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from how_diverse import dataset1  # Assuming you have the dataset1 available

# Create a copy of the dataset to avoid SettingWithCopyWarning
df_selected = dataset1.copy()

# Encode categorical variables
label_encoder = LabelEncoder()
df_selected['Sex'] = label_encoder.fit_transform(df_selected['Sex'])
df_selected['RaceDesc'] = label_encoder.fit_transform(df_selected['RaceDesc'])
df_selected['PerformanceScore'] = label_encoder.fit_transform(df_selected['PerformanceScore'])

# Define features and target variable
features = ['EmpSatisfaction', 'PerformanceScore', 'EngagementSurvey']
target = 'Termd'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df_selected[features], df_selected[target], test_size=0.2, random_state=42)

# Initialize and train the XGBoost model
model = XGBClassifier(random_state=42)
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_report = classification_report(y_test, y_pred)

# Print results
print(f'Accuracy: {accuracy}')
print(f'Confusion Matrix:\n{conf_matrix}')
print(f'Classification Report:\n{classification_report}')