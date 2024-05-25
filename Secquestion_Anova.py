import pandas as pd
from scipy.stats import f_oneway
from how_diverse import dataset1

def perform_anova(dataset1, race_column, salary_column):
    races = dataset1['RaceDesc'].unique()
    
    # Create an empty list to store salary data for each race
    salary_data_by_race = []

    # Iterate over each race
    for race in races:
        salary_data_by_race.append(dataset1[dataset1['RaceDesc'] == race]['Salary'])

    # Perform ANOVA
    anova_result = f_oneway(*salary_data_by_race)

    # Print results
    print(f"ANOVA for Salaries across {'RaceDesc'}: {anova_result}")

# Load your dataset
# Assuming you have a DataFrame named 'data' with columns 'Salary', 'Race', etc.
# Modify column names accordingly based on your dataset

# Call the function
perform_anova(dataset1, race_column='RaceDesc', salary_column='Salary')


#--------------------------------------------------------------------------------

# The Same for the gender


def perform_anova(dataset1, race_column, salary_column):
    genders = dataset1['Sex'].unique()
    
    # Create an empty list to store salary data for each race
    salary_data_by_gender = []

    # Iterate over each race
    for gender in genders:
        salary_data_by_gender.append(dataset1[dataset1['Sex'] == gender]['Salary'])

    # Perform ANOVA
    anova_result = f_oneway(*salary_data_by_gender)

    # Print results
    print(f"ANOVA for Salaries across {'Sex'}: {anova_result}")

# Load your dataset
# Assuming you have a DataFrame named 'data' with columns 'Salary','Sex', etc.
# Modify column names accordingly based on your dataset

# Call the function
perform_anova(dataset1, race_column='Sex', salary_column='Salary')

#-------------------------------------------------------------------------

#For employee Engagement 

def perform_anova(dataset1, race_column, salary_column):
    races = dataset1['RaceDesc'].unique()
    
    # Create an empty list to store salary data for each race
    engagement_data_by_race = []

    # Iterate over each race
    for race in races:
        engagement_data_by_race.append(dataset1[dataset1['RaceDesc'] == race]['EngagementSurvey'])

    # Perform ANOVA
    anova_result = f_oneway(*engagement_data_by_race)

    # Print results
    print(f"ANOVA for Engagement across {'RaceDesc'}: {anova_result}")

# Load your dataset
# Assuming you have a DataFrame named 'data' with columns 'Salary', 'Race', etc.
# Modify column names accordingly based on your dataset

# Call the function
perform_anova(dataset1, race_column='RaceDesc', salary_column='EngagementSurvey')


#--------------------------------------------------------------------------------

# The Same for the gender


def perform_anova(dataset1, race_column, salary_column):
    genders = dataset1['Sex'].unique()
    
    # Create an empty list to store salary data for each race
    engagement_data_by_gender = []

    # Iterate over each race
    for gender in genders:
        engagement_data_by_gender.append(dataset1[dataset1['Sex'] == gender]['EngagementSurvey'])

    # Perform ANOVA
    anova_result = f_oneway(*engagement_data_by_gender)

    # Print results
    print(f"ANOVA for Engagement across {'Sex'}: {anova_result}")

# Load your dataset
# Assuming you have a DataFrame named 'data' with columns 'Salary','Sex', etc.
# Modify column names accordingly based on your dataset

# Call the function
perform_anova(dataset1, race_column='Sex', salary_column='EngagementSurvey')