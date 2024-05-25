import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
dataset1 = pd.read_csv("C:\\Users\\HP\\Desktop\\Technical_task\\HRDataset_v14.csv")

# Drop duplicates if necessary
dataset1 = dataset1.drop_duplicates()

# Convert 'DOB' to datetime format
dataset1['DOB'] = pd.to_datetime(dataset1['DOB'], format='%m/%d/%y', errors='coerce')

# Calculate age based on the current date
current_date = datetime.strptime('01/30/2023', '%m/%d/%Y')
Age = ((current_date - dataset1['DOB']).dt.total_seconds() / (365.25 * 24 * 3600)).abs().astype('int')

# Define the age bins
bins = [27, 31, 36, 42, 47, 53]

# Create a new column 'AgeGroup' with the corresponding bin labels
dataset1['AgeGroup'] = pd.cut(Age, bins=bins, labels=['27-31', '32-36', '37-42', '43-47', '48-53'], include_lowest=True)

# Group by 'Department' and 'AgeGroup' and get the count of employees in each group
age_group_counts = dataset1.groupby(['Department', 'AgeGroup']).size().unstack(fill_value=0)

# Display the DataFrame with age
age_diversity = age_group_counts.sort_index()

# Create a summary table for gender diversity
gender_diversity = dataset1.groupby(['Department', 'Sex']).size().unstack(fill_value=0)
gender_diversity.columns.name = 'Gender Diversity'

# Create a summary table for age diversity
age_diversity_table = dataset1.groupby(['Department', 'AgeGroup']).size().unstack(fill_value=0)
age_diversity_table.columns.name = 'Age Diversity'

# Create a summary table for race diversity
race_diversity = dataset1.groupby(['Department', 'RaceDesc']).size().unstack(fill_value=0)
race_diversity.columns.name = 'Race Diversity'

# Print the results
print("Gender Diversity:")
print(gender_diversity)
print("\nAge Diversity:")
print(age_diversity_table)
print("\nRace Diversity:")
print(race_diversity)

# --------------------------------------------------------------------------------
# Graphical visualization of the results:

# Set style for seaborn
sns.set(style="whitegrid")

# Plot Gender Diversity
plt.figure(figsize=(12, 6))
sns.countplot(x="Department", hue="Sex", data=dataset1)
plt.title("Gender Diversity by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.legend(title="Gender")
plt.show()

# Plot Age Diversity
plt.figure(figsize=(12, 6))
sns.countplot(x="Department", hue='AgeGroup', data=dataset1)
plt.title("Age Diversity by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.legend(title="Age Group")
plt.show()

# Plot Race Diversity
plt.figure(figsize=(14, 6))
sns.countplot(x="Department", hue="RaceDesc", data=dataset1)
plt.title("Race Diversity by Department")
plt.xlabel("Department")
plt.ylabel("Count")
plt.legend(title="Department")
plt.xticks(rotation=45)
plt.show()