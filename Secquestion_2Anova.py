import pandas as pd
from scipy.stats import f_oneway
import seaborn as sns
import matplotlib.pyplot as plt
from how_diverse import dataset1

def perform_anova(dataset1, race_column, salary_column):
    races = dataset1[race_column].unique()
    
    # Create an empty list to store salary data for each race
    salary_data_by_race = []

    # Iterate over each race
    for race in races:
        salary_data_by_race.append(dataset1[dataset1[race_column] == race][salary_column])

    # Perform ANOVA
    anova_result = f_oneway(*salary_data_by_race)

    # Print results
    print(f"ANOVA for Salaries across {race_column}: {anova_result}")

    # Create box plot for visualization
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=race_column, y=salary_column, data=dataset1)
    plt.title(f"Salary Distribution across {race_column}")
    plt.show()

# Load your dataset
# Assuming you have a DataFrame named 'data' with columns 'Salary', 'RaceDesc', etc.
# Modify column names accordingly based on your dataset

# Call the function
perform_anova(dataset1, race_column='RaceDesc', salary_column='Salary')

#---------------------------------------------------------------------------

def perform_anova(dataset, gender_column, salary_column):
    genders = dataset[gender_column].unique()
    
    # Create an empty list to store salary data for each gender
    salary_data_by_gender = []

    # Iterate over each gender
    for gender in genders:
        salary_data_by_gender.append(dataset[dataset[gender_column] == gender][salary_column])

    # Perform ANOVA
    anova_result = f_oneway(*salary_data_by_gender)

    # Print results
    print(f"ANOVA for Salaries across {gender_column}: {anova_result}")

    # Create a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=gender_column, y=salary_column, data=dataset)
    plt.title(f'Box Plot of Salaries by {gender_column}')
    plt.xlabel(gender_column)
    plt.ylabel(salary_column)
    plt.show()

# Call the function
perform_anova(dataset1, gender_column='Sex', salary_column='Salary')

# ----------------------------------------------------------------

def perform_anova(dataset, race_column, engagement_column):
    races = dataset[race_column].unique()
    
    # Create an empty list to store engagement data for each race
    engagement_data_by_race = []

    # Iterate over each race
    for race in races:
        engagement_data_by_race.append(dataset[dataset[race_column] == race][engagement_column])

    # Perform ANOVA
    anova_result = f_oneway(*engagement_data_by_race)

    # Print results
    print(f"ANOVA for Engagement across {race_column}: {anova_result}")

    # Create a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=race_column, y=engagement_column, data=dataset)
    plt.title(f'Box Plot of Engagement by {race_column}')
    plt.xlabel(race_column)
    plt.ylabel(engagement_column)
    plt.show()

# Call the function
perform_anova(dataset1, race_column='RaceDesc', engagement_column='EngagementSurvey')

# --------------------------------------------------------------------

def perform_anova(dataset, gender_column, engagement_column):
    genders = dataset[gender_column].unique()
    
    # Create an empty list to store engagement data for each gender
    engagement_data_by_gender = []

    # Iterate over each gender
    for gender in genders:
        engagement_data_by_gender.append(dataset[dataset[gender_column] == gender][engagement_column])

    # Perform ANOVA
    anova_result = f_oneway(*engagement_data_by_gender)

    # Print results
    print(f"ANOVA for Engagement across {gender_column}: {anova_result}")

    # Create a box plot
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=gender_column, y=engagement_column, data=dataset)
    plt.title(f'Box Plot of Engagement by {gender_column}')
    plt.xlabel(gender_column)
    plt.ylabel(engagement_column)
    plt.show()

# Call the function
perform_anova(dataset1, gender_column='Sex', engagement_column='EngagementSurvey')