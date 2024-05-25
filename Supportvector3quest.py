import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import LabelEncoder
from how_diverse import dataset1  # Assuming you have the dataset1 available

# Encode categorical variables if needed
label_encoder = LabelEncoder()
# dataset1['Sex'] = label_encoder.fit_transform(dataset1['Sex'])
# dataset1['RaceDesc'] = label_encoder.fit_transform(dataset1['RaceDesc'])
dataset1['PerformanceScore'] = label_encoder.fit_transform(dataset1['PerformanceScore'])

# Define features and target variable
features = ['EmpSatisfaction']
target = 'Termd'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(dataset1[features], dataset1[target], test_size=0.2, random_state=42)

# Initialize and train the Support Vector Machines (SVM) model
model = SVC(random_state=42)
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