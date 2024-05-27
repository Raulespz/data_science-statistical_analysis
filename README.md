# DATA SCIENCE AND STATISTICAL ANALYSIS APLIYNG PYTHON

## DEI (Diversity, Equity and Inclusion) of an Organization

## INSTRUCTIONS AND THE RESULTS OBTAINED IN THE PRESENT PROJECT:

Using the data set and questions below, conduct the analysis and prepare a short presentation
with your results. Please, send your code (in Python or R) and presentation slides by XX, 2024.
Data Set: ` https://www.kaggle.com/datasets/rhuebner/human-resources-data-set/data `
Using the data set, please answer the following questions for the DEI (Diversity, Equity and
Inclusion) head:
1. How diverse is the organization regarding gender, age, and race? Which departments
are more/less diverse?

About the code is the following in each case:
To count the diversity among the departments:
```bash
org_diversity.py
```
Analyzing the Races through the departments:
```bash
chi-square_races.py
```
Analyzing the gender through the departments:
```bash
chi-square_gender.py
```
to run the code for example in the terminal put python and one of the codes before remarked such: 
```bash
pyhton chi-square_gender.py
```
Organization diversity:
Gender Diversity:
Observations:
The organization exhibits gender diversity, with a mix of male and female employees across
departments. The Production department has a notable gender imbalance, with a higher
number of female employees.
The IT/IS and Sales departments show a relatively balanced gender distribution.

Age Diversity:
In general, I could deduce there is an average on diversity through departments, Although in
Production, Admin office, Sales and IT/IS, have a slightly preference of people through ages
among: 32-42.

Race Diversity:
Observations:
Sales, Admin Offices and Executive Office have the most racially diverse departments, with
representation from multiple racial groups.
Production and IT/IS have lower racial diversity, primarily consisting of employees from the
White racial group.

Departments has and equality Race diversity.
This statistical analysis provides a comprehensive overview of gender, age, and race diversity
within the organization. It forms the basis for targeted interventions to enhance diversity and
inclusion across departments, contributing to a more vibrant and representative workforce.



2. The DEI head is concerned with the lack of equal treatment in the company for diverse
employees (e.g. Black vs. White employees; women vs men) and asks you to verify this
with data on salaries and employee engagement.
What do you conclude based on the available data?
If you could get access to additional information about employees to answer this
question, which variables would you have added to your analysis and why?

For the second question was developed an ANOVA statistical analysis to know the any statistically significant differences among the Salary, Engagement among the race and the age:
Code employed here is:
```bash
Secquestion_Anova.py
```
to make the graphics of this results:
```bash
Secquestion_2Anova.py
```

ANOVA Results:
ANOVA for Salaries across RaceDesc: F_onewayResult(statistic=1.2863499291564824,
pvalue=0.2695646450406912)

ANOVA for Salaries across Sex: F_onewayResult(statistic=0.9754391883261775,
pvalue=0.3241001178974532)

ANOVA for Engagement across RaceDesc: F_onewayResult(statistic=0.6574140163803003,
pvalue=0.6560595963321796)

ANOVA for Engagement across Sex: F_onewayResult(statistic=0.40716864030783856,
pvalue=0.523882696486162)

What do you conclude based on the available data?
If you could get access to additional information about employees to answer this question,
which variables would you have added to your analysis and why?
Salaries Analysis:
RaceDesc:

F-statistic = 1.29
p-value = 0.27
Sex:
F-statistic = 0.98
p-value = 0.32
Interpretation:
For both RaceDesc and Sex, the p-values are greater than the typical significance level of
0.05. Therefore, there are no significant differences in salaries among different races and
genders.
Employee Engagement Analysis:
RaceDesc:
F-statistic = 0.66
p-value = 0.66
Sex:
F-statistic = 0.41
p-value = 0.52
Interpretation:
Similar to the salaries analysis, for both RaceDesc and Sex, the p-values are higher than 0.05.
This suggests that there is no significant difference in employee engagement scores among
different races and genders.
Overall Conclusion:
Based on the available data, there is no statistically significant evidence to conclude that there
are differences in salaries or employee engagement scores among employees of different
races or genders.
Additional Information:
To further investigate and address the DEI head&#39;s concerns, it would be beneficial to include
additional variables in the analysis:
Job Level or Position: Differences in salaries and engagement may be related to job roles.

Education Level: Educational background could impact salaries and engagement.
Years of Experience: Experience might contribute to salary disparities and engagement levels.
Performance Ratings: Analyzing performance ratings can provide insights into merit-based
differences.
Work Hours: Disparities may arise due to variations in working hours.
By including these variables, a more comprehensive analysis can be conducted to identify
potential sources of disparities and inform strategies for promoting equal treatment and
diversity in the company.

3. Could you predict who is more likely to leave the company? How good is your
prediction? What are the main limitations?

To answer this question was carried out a variety of tests to create the better scenario
founding the following results:

XGBBOOST CLASSIFIER:
```bash
xgboost_3quest.py
```
logistic regression:
```bash
logisticreg_3quest.py
```
Support Vector machine:
```bash
Supportvector3quest.py
```
Neural Network:
```bash
neural_netw3quest.py
```
I have developed some models to create the best response possible with the following models:
Model Selection:
Logistic Regression, Support Vector Machine, Decision Trees, Random Forests, neural networks
Boosting.
Although, I could not get an expected result here, with the better that I get a result was:
With the model selection that was approximately but continuing being not sufficient even to
consider it good XGBoost (Review the code for more information regarding to this model).

Interpretation:
The model performance is moderate, but there is room for improvement.
Class 0 predictions (not Termd) are relatively better than class 1 predictions (Termd).
The model has better precision for class 0, indicating fewer false positives for employees not
leaving.
The recall for class 1 is relatively low, suggesting that the model misses some instances of
employees leaving (false negatives).
The F1-score provides a balance between precision and recall.
Considerations for Improvement:
May be possible to explore feature engineering, including additional relevant features.
Try other algorithms or tune hyperparameters to enhance model performance.
My prediction is not even close to good, although regarding to all predicting models carried
this was the most acceptable (in the document of code are the codes of all the models
developed to carried out this question).
The main limitations are some factors that are not taking into a consideration in the database,
as well for other consideration that is particularly of the employees that could not be
possible to include accurate as a measure. Could be necessary as well include features
such: Motivations to be in the job, Performance the work that he has done through his
time in the company and related.

4. The DEI head is again concerned that the attrition risk is higher for Black employees
and women. Do the data and your prediction model support this concern?

Based in the current analysis carried out I could conclude that there is not a significant
difference about race, sex, age, through the statistical analysis and the statistical analysis
corroborate this answer.
Based on the comprehensive analysis conducted on the data and the outcomes of the
prediction model:

Salaries Analysis:
There is no statistically significant evidence of differences in salaries based on race (RaceDesc)
or gender (Sex). Both the F-statistics and p-values for the ANOVA tests indicate that salary
levels are comparable across different racial and gender groups.
Employee Engagement Analysis:

Similar to the salaries analysis, the ANOVA results for employee engagement scores across
race and gender do not show significant differences. The p-values for RaceDesc and Sex are
higher than 0.05, suggesting that there is no substantial variation in employee engagement
among different racial and gender categories.
Attrition Prediction Model:
The predictive models, despite their efforts, show only moderate performance in identifying
employees at risk of leaving. The XGBoost model, while being the most acceptable among the
developed models, still has limitations in terms of precision and recall for employees who
actually leave.
Conclusion:
Based on the available data and the prediction model, there is no substantial support for the
concern that attrition risk is higher for Black employees and women. The statistical analyses
for salaries and employee engagement, along with the predictive model, indicate no significant
disparities among different racial and gender groups.
Additional Considerations for Improvement:
To further address the DEI head concerns, additional information could be incorporated into
the analysis, such as job level, education level, years of experience, performance ratings, and
work hours.
Continuously refining the attrition prediction model by exploring feature engineering, trying
alternative algorithms, and tuning hyperparameters can enhance its accuracy.
It is important to acknowledge the limitations of the current dataset and recognize that certain
factors influencing attrition risk may not be fully captured.
In summary, the available data and analysis results do not strongly support the concern of
higher attrition risk for Black employees and women. However, ongoing efforts to refine
predictive models and incorporate additional variables will contribute to a more
comprehensive understanding of employee attrition within the organization.
