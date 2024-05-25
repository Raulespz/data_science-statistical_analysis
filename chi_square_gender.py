import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency
from how_diverse import dataset1

# Load your dataset
# Assuming your dataset has a column 'Department' and 'RaceDesc'
# Example:
# dataset = pd.read_csv('your_dataset.csv')

# Create a contingency table
contingency_table = pd.crosstab(dataset1['Department'], dataset1['Sex'])

# Print the contingency table
print("Contingency Table:")
print(contingency_table)

# Perform chi-square test for independence
chi2_stat, p_value, _, _ = chi2_contingency(contingency_table)

# Print the results
print(f"\nChi-square Statistic: {chi2_stat}")
print(f"P-value: {p_value}")

# Interpret the results
alpha = 0.05  # significance level
print(f"\nSignificance Level: {alpha}")
print("Result:")
if p_value < alpha:
    print(" Ha: Reject the null hypothesis. Departments has gender equity")
else:
    print(" Ho: Do not Reject the null hypothesis. Departments has not gender equity")


# Create a bar chart for the contingency table
fig, ax = plt.subplots(figsize=(10, 6))
contingency_table.plot(kind='bar', stacked=True, colormap='viridis', ax=ax)
plt.title('Gender Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.legend(title='Sex', bbox_to_anchor=(1, 1))

# Create a bar chart for the contingency table
contingency_table.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Gender Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Count')
plt.legend(title='Gender', bbox_to_anchor=(1, 1))

# Save the plot to a file or display it
plt.savefig('gender_distribution_by_department.png', bbox_inches='tight')
plt.show()