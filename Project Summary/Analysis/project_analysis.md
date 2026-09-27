# Employee Performance Analysis
## Project Analysis

## 1. Project Overview

This project analyzes employee performance data from INX Future Inc. to understand the factors associated with employee performance and to develop a machine learning model capable of predicting employee PerformanceRating.

The analysis follows a structured data science workflow covering data understanding, data preprocessing, exploratory data analysis, statistical testing, machine learning model comparison, hyperparameter tuning, feature importance analysis, employee performance prediction, and visualization.

The analysis uses the employee-level dataset supplied as part of the IABAC Certified Data Scientist project.

---

## 2. Dataset Overview

The dataset contains **1,200 employee records and 28 columns** in the original source data.

The variables contain information related to:

- Employee demographics
- Education
- Department and job role
- Business travel
- Distance from home
- Job characteristics
- Job involvement and satisfaction
- Salary hike
- Work experience
- Training
- Work-life balance
- Attrition
- Employee performance

The target variable is:

`PerformanceRating`

The observed target categories in the dataset are:

- `2` — Good
- `3` — Excellent
- `4` — Outstanding

There are no missing values or duplicate records in the supplied dataset.

The target distribution is imbalanced:

| Performance Rating | Employees | Percentage |
|---:|---:|---:|
| 2 | 194 | 16.17% |
| 3 | 874 | 72.83% |
| 4 | 132 | 11.00% |
| **Total** | **1,200** | **100.00%** |

Because Rating 3 represents the majority of observations, model evaluation considers class-balanced metrics such as Balanced Accuracy, Macro Precision, Macro Recall, and Macro F1 in addition to overall Accuracy.

---

## 3. Data Processing

The original dataset was loaded from the supplied Excel workbook.

The raw dataset was preserved separately and was not modified directly.

A working copy was created for data validation and preparation.

The following checks were performed:

- Dataset dimensions
- Column names and data types
- Missing values
- Duplicate records
- Categorical value consistency
- Target-value validity
- Logical consistency among employee experience variables
- Variable-level understanding using the supplied Data Definitions sheet

No employee records were removed during preprocessing because the validation checks did not identify missing values, duplicate records, invalid target values, or logical inconsistencies requiring row removal.

A canonical processed dataset was then created for subsequent exploratory analysis and model development.

---

## 4. Feature Classification

The identifier `EmpNumber` was excluded from machine learning because it identifies employees rather than representing a meaningful performance-related predictor.

The remaining predictors were organized into three groups.

### 4.1 Ordinal Features

The following variables represent ordered categories:

- `EmpEducationLevel`
- `EmpEnvironmentSatisfaction`
- `EmpJobInvolvement`
- `EmpJobSatisfaction`
- `EmpRelationshipSatisfaction`
- `EmpWorkLifeBalance`

These variables were retained in their numerical ordinal form so that their ordering was preserved.

### 4.2 Nominal Categorical Features

The following variables were treated as nominal categorical variables:

- `Gender`
- `EducationBackground`
- `MaritalStatus`
- `EmpDepartment`
- `EmpJobRole`
- `BusinessTravelFrequency`
- `OverTime`
- `Attrition`

These variables were converted to machine-readable representations using one-hot encoding during model preprocessing.

### 4.3 Numerical Features

The numerical predictors include:

- `Age`
- `DistanceFromHome`
- `EmpHourlyRate`
- `EmpJobLevel`
- `NumCompaniesWorked`
- `EmpLastSalaryHikePercent`
- `TotalWorkExperienceInYears`
- `TrainingTimesLastYear`
- `ExperienceYearsAtThisCompany`
- `ExperienceYearsInCurrentRole`
- `YearsSinceLastPromotion`
- `YearsWithCurrManager`

A total of **26 predictor variables** were used for modeling.

---

## 5. Feature Engineering and Transformation

No new derived business features were created because the supplied variables already provided direct information relevant to employee performance.

The main preprocessing transformations were performed within machine learning pipelines.

For models requiring scaled numerical inputs, numerical and ordinal variables were standardized using `StandardScaler`.

Categorical variables were transformed using `OneHotEncoder` with `handle_unknown="ignore"`.

Two preprocessing pipelines were maintained:

- A scaled preprocessing pipeline for Logistic Regression, K-Nearest Neighbors, Support Vector Machine, and Naive Bayes.
- A tree-model preprocessing pipeline without numerical scaling for Decision Tree, Random Forest, Gradient Boosting, and XGBoost.

The preprocessing pipeline was fitted using the training data and applied consistently to the test data.

After preprocessing, the feature representation contained **61 model features**, because categorical variables were expanded through one-hot encoding.

---

## 6. Train-Test Experimental Design

The data was divided into training and testing sets using an **80:20 stratified split**.

`random_state=42` was used to make the split reproducible.

Stratification was applied so that the relative distribution of PerformanceRating classes remained similar in the training and testing datasets.

The resulting datasets contained:

- Training set: 960 employees
- Test set: 240 employees

The same train-test split was used for the evaluated classification models to provide a consistent basis for comparison.

## 7. Exploratory Data Analysis and Statistical Findings

Exploratory data analysis was performed to understand the distribution of employee performance and to identify relationships between employee attributes and `PerformanceRating`.

Both categorical and numerical/ordinal variables were examined.

---

## 7.1 Performance Rating Distribution

The target variable is imbalanced, with Rating 3 representing the majority of employees.

- Rating 2: 194 employees (16.17%)
- Rating 3: 874 employees (72.83%)
- Rating 4: 132 employees (11.00%)

Therefore, model evaluation was not based on Accuracy alone. Macro-level and class-balanced metrics were also considered.

---

## 7.2 Department-wise Performance

Performance Rating 3 is the dominant category across every department, but the proportions of Ratings 2 and 4 vary between departments.

| Department | Rating 2 | Rating 3 | Rating 4 |
|---|---:|---:|---:|
| Data Science | 5.00% | 85.00% | 10.00% |
| Development | 3.60% | 84.21% | 12.19% |
| Finance | 30.61% | 61.22% | 8.16% |
| HR | 18.52% | 70.37% | 11.11% |
| R&D | 19.83% | 68.22% | 11.95% |
| Sales | 23.32% | 67.29% | 9.38% |

Finance has the highest proportion of Rating 2 employees among the departments, while Development has the highest proportion of Rating 4 employees.

The Data Science department contains only 20 employees, so its percentages should be interpreted with caution because of the smaller sample size.

---

## 7.3 Categorical Variable Significance Testing

Chi-square tests of independence were used to examine whether categorical variables showed statistically significant associations with `PerformanceRating`.

Using a significance level of 0.05, the following variables showed statistically significant associations:

| Variable | p-value | Result |
|---|---:|---|
| `EmpDepartment` | < 0.0001 | Significant |
| `EmpJobRole` | < 0.0001 | Significant |
| `OverTime` | 0.0035 | Significant |

The following categorical variables did not show statistically significant associations at the 0.05 level:

| Variable | p-value |
|---|---:|
| `MaritalStatus` | 0.1894 |
| `Attrition` | 0.2771 |
| `BusinessTravelFrequency` | 0.3549 |
| `EducationBackground` | 0.4216 |
| `Gender` | 0.9218 |

A statistically non-significant result in this analysis does not establish that a variable has no predictive value under every modeling approach; it indicates that the tested categorical association was not statistically significant at the selected significance level.

---

## 7.4 Numerical and Ordinal Variable Significance Testing

Kruskal-Wallis tests were used to examine differences in the distributions of numerical and ordinal variables across PerformanceRating categories.

The following variables showed statistically significant differences at the 0.05 level:

| Variable | p-value |
|---|---:|
| `EmpEnvironmentSatisfaction` | < 0.0001 |
| `EmpLastSalaryHikePercent` | < 0.0001 |
| `YearsSinceLastPromotion` | < 0.0001 |
| `ExperienceYearsInCurrentRole` | < 0.0001 |
| `EmpWorkLifeBalance` | 0.0001 |
| `YearsWithCurrManager` | < 0.0001 |
| `ExperienceYearsAtThisCompany` | < 0.0001 |
| `EmpJobLevel` | 0.0038 |
| `TotalWorkExperienceInYears` | 0.0085 |

The following variables did not show statistically significant differences at the 0.05 level:

- `Age`
- `DistanceFromHome`
- `EmpHourlyRate`
- `NumCompaniesWorked`
- `TrainingTimesLastYear`
- `EmpJobInvolvement`
- `EmpRelationshipSatisfaction`
- `EmpEducationLevel`
- `EmpJobSatisfaction`

---

## 7.5 Correlation Analysis

Correlation analysis was used to examine the direction and strength of linear relationships between numerical/ordinal variables and `PerformanceRating`.

The strongest observed correlations with PerformanceRating were:

| Variable | Correlation with PerformanceRating |
|---|---:|
| `EmpEnvironmentSatisfaction` | +0.396 |
| `EmpLastSalaryHikePercent` | +0.334 |
| `YearsSinceLastPromotion` | -0.168 |
| `ExperienceYearsInCurrentRole` | -0.148 |
| `EmpWorkLifeBalance` | +0.124 |
| `YearsWithCurrManager` | -0.122 |
| `ExperienceYearsAtThisCompany` | -0.112 |
| `EmpJobLevel` | -0.077 |
| `TotalWorkExperienceInYears` | -0.068 |

The remaining numerical/ordinal variables showed relatively weak correlations with the target.

Correlation measures association and does not establish causation.

---

## 7.6 Environment Satisfaction and Performance

`EmpEnvironmentSatisfaction` showed one of the clearest relationships with employee performance.

The observed PerformanceRating distribution within each environment satisfaction level was:

| Environment Satisfaction | Rating 2 | Rating 3 | Rating 4 |
|---|---:|---:|---:|
| 1 - Low | 39.13% | 55.22% | 5.65% |
| 2 - Medium | 40.50% | 53.72% | 5.79% |
| 3 - High | 0.82% | 84.47% | 14.71% |
| 4 - Very High | 0.83% | 85.04% | 14.13% |

Employees with satisfaction levels 1 and 2 have substantially larger proportions of Rating 2, while levels 3 and 4 are predominantly Rating 3 and contain a larger proportion of Rating 4.

This variable was also identified as the second most important feature by the tuned XGBoost model.

---

## 7.7 Salary Hike and Performance

`EmpLastSalaryHikePercent` showed a statistically significant relationship with PerformanceRating and was also among the important predictive variables identified by the machine learning model.

The average salary hike percentages by performance rating were examined to understand how recent salary increases differed across the target categories.

The analysis showed a higher average salary hike among employees with Rating 4 compared with the lower performance categories.

This represents an observed relationship in the dataset and should not be interpreted as evidence that salary increases directly cause higher employee performance.

---

## 7.8 Multivariate Relationship

A multivariate analysis was performed using `EmpEnvironmentSatisfaction` together with `EmpLastSalaryHikePercent`.

The analysis showed that employees with higher environment satisfaction levels had very few Rating 2 observations, while employees receiving Rating 4 generally showed higher salary-hike percentages than employees receiving Rating 3.

For environment satisfaction levels 3 and 4, only three Rating 2 observations were present at each level.

This indicates that multiple employee attributes may provide complementary information when predicting performance rather than relying on a single variable.

The observed relationship is descriptive and does not establish causality.

---

## 7.9 Key Exploratory Findings

The exploratory and statistical analysis identified several important patterns:

1. Performance Rating 3 is the dominant category across the complete dataset and across every department.

2. Department and job role show statistically significant associations with PerformanceRating.

3. OverTime also shows a statistically significant association with PerformanceRating.

4. Environment satisfaction has one of the strongest relationships with PerformanceRating among the numerical and ordinal variables examined.

5. Salary hike percentage is positively associated with PerformanceRating and differs across performance categories.

6. Several experience-related variables, including `YearsSinceLastPromotion`, `ExperienceYearsInCurrentRole`, `ExperienceYearsAtThisCompany`, and `YearsWithCurrManager`, show statistically significant differences across performance-rating groups.

7. The exploratory analysis indicates relationships between employee attributes and performance, but these relationships should not be interpreted as causal effects.

## 8. Feature Selection and Important Factors

Feature selection was performed using a combination of exploratory analysis, statistical testing, correlation analysis, and model-based feature importance.

Rather than removing variables solely on the basis of a single statistical test, the available predictors were retained for model comparison and their predictive contribution was evaluated using the tuned XGBoost model.

The identifier `EmpNumber` was excluded because it is an employee identifier and does not represent a meaningful predictive attribute.

---

## 8.1 Model-Based Feature Importance

The tuned XGBoost model was used to identify the relative importance of the original predictor variables.

Because categorical variables were one-hot encoded during preprocessing, the importance values of their individual encoded categories were aggregated back to their original feature names.

The resulting feature importance ranking was:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | `EmpJobRole` | 0.160347 |
| 2 | `EmpEnvironmentSatisfaction` | 0.137851 |
| 3 | `EmpDepartment` | 0.121276 |
| 4 | `EmpLastSalaryHikePercent` | 0.107597 |
| 5 | `YearsSinceLastPromotion` | 0.097228 |
| 6 | `EducationBackground` | 0.053696 |
| 7 | `ExperienceYearsInCurrentRole` | 0.039213 |
| 8 | `OverTime` | 0.031020 |
| 9 | `BusinessTravelFrequency` | 0.028977 |
| 10 | `EmpWorkLifeBalance` | 0.021407 |
| 11 | `MaritalStatus` | 0.020264 |
| 12 | `Gender` | 0.019490 |
| 13 | `YearsWithCurrManager` | 0.018192 |
| 14 | `ExperienceYearsAtThisCompany` | 0.016617 |
| 15 | `TrainingTimesLastYear` | 0.014368 |
| 16 | `EmpRelationshipSatisfaction` | 0.013174 |
| 17 | `Attrition` | 0.011843 |
| 18 | `DistanceFromHome` | 0.011361 |
| 19 | `EmpJobSatisfaction` | 0.011348 |
| 20 | `TotalWorkExperienceInYears` | 0.010886 |
| 21 | `EmpHourlyRate` | 0.010447 |
| 22 | `EmpJobInvolvement` | 0.010064 |
| 23 | `Age` | 0.009263 |
| 24 | `EmpJobLevel` | 0.008411 |
| 25 | `NumCompaniesWorked` | 0.007876 |
| 26 | `EmpEducationLevel` | 0.007783 |

The three highest-ranked features were:

1. `EmpJobRole`
2. `EmpEnvironmentSatisfaction`
3. `EmpDepartment`

Together, these three features account for approximately **41.95%** of the aggregated model-based feature importance.

---

## 8.2 Important Factor 1: Employee Job Role

`EmpJobRole` was the most important feature according to the tuned XGBoost model, with an aggregated importance of approximately **16.03%**.

The distribution of PerformanceRating varies considerably across job roles.

For example:

- Business Analyst: 81.25% Rating 3 and 18.75% Rating 4
- Finance Manager: 30.61% Rating 2, 61.22% Rating 3, and 8.16% Rating 4
- Manager: 23.53% Rating 2, 56.86% Rating 3, and 19.61% Rating 4
- Technical Architect: 100% Rating 3
- Delivery Manager: 100% Rating 3

These differences indicate that job role contains substantial predictive information about employee performance within this dataset.

The results describe patterns observed in the supplied employee data and should not be interpreted as evidence that a particular job role causes a specific performance rating.

---

## 8.3 Important Factor 2: Environment Satisfaction

`EmpEnvironmentSatisfaction` was the second most important feature, with an aggregated importance of approximately **13.79%**.

The exploratory analysis also identified a strong relationship between environment satisfaction and PerformanceRating.

Employees with lower environment satisfaction levels had substantially larger proportions of Rating 2:

- Satisfaction Level 1: 39.13% Rating 2
- Satisfaction Level 2: 40.50% Rating 2

In comparison:

- Satisfaction Level 3: 0.82% Rating 2 and 14.71% Rating 4
- Satisfaction Level 4: 0.83% Rating 2 and 14.13% Rating 4

The Kruskal-Wallis test also identified a statistically significant difference in environment satisfaction across PerformanceRating groups, with p-value < 0.0001.

Therefore, environment satisfaction represents an important observed predictor in both the statistical analysis and the machine learning model.

---

## 8.4 Important Factor 3: Employee Department

`EmpDepartment` was the third most important feature, with an aggregated importance of approximately **12.13%**.

Performance distributions differed across departments.

Finance had the highest observed proportion of Rating 2 employees at 30.61%, while Development had the highest observed proportion of Rating 4 employees at 12.19%.

The chi-square test also showed a statistically significant association between `EmpDepartment` and `PerformanceRating` with p-value < 0.0001.

These findings indicate that department provides useful predictive information for employee performance in the supplied dataset.

The Data Science department contains only 20 employees, so its percentages should be interpreted cautiously because of the smaller sample size.

---

## 8.5 Additional Important Factors

Other variables also contributed meaningful predictive information.

`EmpLastSalaryHikePercent` was the fourth-ranked feature with an importance of approximately 10.76%. It also showed a statistically significant relationship with PerformanceRating.

`YearsSinceLastPromotion` was the fifth-ranked feature with an importance of approximately 9.72% and showed a statistically significant difference across performance-rating groups.

`EducationBackground` and `ExperienceYearsInCurrentRole` were also among the higher-ranked predictors.

`OverTime` had a lower model-based importance than the top three factors but showed a statistically significant categorical association with PerformanceRating.

---

## 8.6 Feature Importance and Statistical Findings

The feature-selection analysis combines two complementary perspectives.

Statistical testing identifies variables for which differences or associations with PerformanceRating are detectable under the selected statistical tests.

Model-based feature importance measures how useful variables are to the tuned XGBoost model when making predictions.

The two approaches do not have to produce identical rankings.

For example, `EmpEnvironmentSatisfaction`, `EmpLastSalaryHikePercent`, and several experience-related variables showed statistically significant relationships with the target and also received meaningful model importance.

At the same time, some variables that were not statistically significant in the individual tests can still contribute predictive information when considered together with other variables in a machine learning model.

---

## 8.7 Important Interpretation

The top three factors identified by the tuned XGBoost model are:

- `EmpJobRole`
- `EmpEnvironmentSatisfaction`
- `EmpDepartment`

These factors should be interpreted as **important predictive variables in this dataset**, rather than as proven causes of employee performance.

The feature-importance analysis describes how the trained model uses the available information for prediction. It does not establish causal relationships between employee characteristics and performance.

In addition, some of the predictors, such as `EmpEnvironmentSatisfaction` and `Attrition`, describe existing employees and may not be directly available when evaluating external candidates during hiring.

Therefore, their use in a hiring-oriented prediction system should be considered carefully.

## 9. Machine Learning Model Development and Evaluation

A supervised multiclass classification approach was used to predict `PerformanceRating`.

The objective was to develop a model capable of predicting the observed employee performance categories:

- Rating 2 — Good
- Rating 3 — Excellent
- Rating 4 — Outstanding

Multiple classification algorithms were evaluated using the same training and testing datasets.

---

## 9.1 Classification Algorithms Evaluated

The following eight classification algorithms were evaluated:

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Support Vector Machine
- Naive Bayes
- Gradient Boosting
- XGBoost

These algorithms provide different modeling approaches, including linear classification, distance-based classification, probabilistic classification, decision trees, ensemble learning, and gradient boosting.

---

## 9.2 Handling the Imbalanced Target

The target variable contains substantially more Rating 3 observations than Rating 2 and Rating 4 observations.

To reduce the effect of class imbalance during model training, class-balanced weighting was used for the applicable algorithms.

Model performance was evaluated using metrics that consider all performance-rating classes rather than relying only on overall accuracy.

The primary comparison metrics included:

- Accuracy
- Balanced Accuracy
- Macro Precision
- Macro Recall
- Macro F1
- Five-fold Stratified Cross-Validation Macro F1

Macro F1 was given particular importance because it gives equal importance to each performance-rating class.

---

## 9.3 Baseline Model Evaluation

All models were trained using the same 80:20 stratified train-test split.

The baseline test-set results were:

| Model | Accuracy | Balanced Accuracy | Macro Precision | Macro Recall | Macro F1 | CV Macro F1 |
|---|---:|---:|---:|---:|---:|---:|
| Gradient Boosting | 92.92% | 86.23% | 91.34% | 86.23% | 88.56% | 89.32% |
| XGBoost | 92.92% | 85.56% | 91.93% | 85.56% | 88.45% | 88.82% |
| Random Forest | 92.08% | 84.75% | 89.64% | 84.75% | 86.98% | 87.97% |
| Decision Tree | 91.25% | 87.41% | 87.93% | 87.41% | 87.65% | 82.10% |
| Support Vector Machine | 76.25% | 75.76% | 66.16% | 75.76% | 69.09% | 69.46% |
| Logistic Regression | 75.83% | 75.76% | 65.19% | 75.76% | 68.69% | 66.85% |
| K-Nearest Neighbors | 76.25% | 48.90% | 69.35% | 48.90% | 53.13% | 49.32% |
| Naive Bayes | 20.42% | 44.78% | 45.92% | 44.78% | 20.97% | 22.20% |

The tree-based ensemble methods, particularly Gradient Boosting, XGBoost, and Random Forest, produced stronger overall results than the other evaluated approaches.

Five-fold Stratified Cross-Validation was used to assess whether model performance was reasonably consistent across different training folds.

---

## 9.4 Hyperparameter Tuning

The three leading baseline ensemble models were selected for further hyperparameter tuning:

- Gradient Boosting
- Random Forest
- XGBoost

`GridSearchCV` with five-fold cross-validation was used for hyperparameter tuning.

Macro F1 was used as the optimization metric so that the minority performance-rating classes were considered during model selection.

The best cross-validation results were:

| Model | Best CV Macro F1 |
|---|---:|
| XGBoost | 0.9041 |
| Gradient Boosting | 0.8966 |
| Random Forest | 0.8819 |

The selected XGBoost configuration was:

- `n_estimators = 200`
- `max_depth = 4`
- `learning_rate = 0.03`
- `subsample = 1.0`

---

## 9.5 Tuned Model Test Performance

The tuned models were evaluated on the same held-out test set.

| Model | Accuracy | Balanced Accuracy | Macro Precision | Macro Recall | Macro F1 |
|---|---:|---:|---:|---:|---:|
| XGBoost | 93.75% | 87.04% | 93.62% | 87.04% | 90.03% |
| Gradient Boosting | 93.33% | 87.51% | 92.25% | 87.51% | 89.66% |
| Random Forest | 92.50% | 84.95% | 91.02% | 84.95% | 87.64% |

The tuned XGBoost model achieved a test-set Macro F1 of **90.03%** and a tuned five-fold cross-validation Macro F1 of **90.41%**.

The close relationship between the cross-validation result and the held-out test performance provides evidence that the selected model performed consistently across the evaluation procedure.

---

## 9.6 Final XGBoost Class-wise Performance

The final tuned XGBoost model produced the following class-wise results on the test set:

| Performance Rating | Precision | Recall | F1-Score |
|---:|---:|---:|---:|
| 2 | 0.91 | 0.82 | 0.86 |
| 3 | 0.94 | 0.98 | 0.96 |
| 4 | 0.95 | 0.81 | 0.88 |

The model achieved particularly high recall for Rating 3.

Ratings 2 and 4 had lower recall than Rating 3, which is consistent with their smaller representation in the dataset.

Therefore, class-wise performance should be considered alongside overall accuracy when interpreting the model.

---

## 9.7 Final Model Selection

The tuned XGBoost model was selected as the final model for the prediction stage.

The final recorded evaluation results were:

- Accuracy: **93.75%**
- Balanced Accuracy: **87.04%**
- Macro Precision: **93.62%**
- Macro Recall: **87.04%**
- Macro F1: **90.03%**
- Five-fold tuned Cross-Validation Macro F1: **90.41%**

The complete preprocessing and XGBoost model pipeline was saved as:

`final_xgboost_employee_performance_model.joblib`

Saving the complete pipeline ensures that the preprocessing operations used during training can also be applied consistently when new employee records are provided for prediction.

---

## 9.8 Model Evaluation Interpretation

The evaluation indicates that the final model can predict the three observed PerformanceRating categories with high performance on the supplied test dataset.

However, the model should be interpreted within the limitations of the available data.

The test results are based on a single held-out test set from the supplied dataset, while cross-validation was used as an additional assessment of model consistency.

The model's predictions represent estimated performance-rating categories based on the available employee attributes. They should not be interpreted as guaranteed employee outcomes.

In addition, the dataset represents existing employees. Some predictors, such as `EmpEnvironmentSatisfaction` and `Attrition`, may not be available or appropriate when assessing an external candidate during the hiring process.

Therefore, further validation using appropriate candidate-level data would be required before applying the model to an actual hiring process.
## 10. Prediction System

A separate prediction notebook was developed to demonstrate how the trained model can be used to predict employee performance for new employee records.

The prediction workflow uses the complete saved XGBoost pipeline generated during model training.

---

## 10.1 Loading the Saved Model

The saved model pipeline was loaded from:

`models/final_xgboost_employee_performance_model.joblib`

The complete pipeline was saved rather than only the XGBoost classifier.

This allows the same preprocessing operations used during model training to be applied automatically to new input records.

---

## 10.2 Prediction Inputs

The prediction system accepts the same **26 predictor variables** used during model training.

These include:

- Demographic attributes
- Education-related attributes
- Department and job role
- Business travel
- Distance from home
- Job characteristics
- Satisfaction and involvement measures
- Salary hike percentage
- Work experience
- Training
- Work-life balance
- Attrition

The employee identifier `EmpNumber` is not required as a prediction input because it was excluded from model training.

---

## 10.3 Input Validation

Input validation was implemented before generating predictions.

The prediction notebook checks whether the supplied input contains the expected predictor variables.

The validation verifies:

- Expected number of features: 26
- Actual number of supplied features
- Missing expected columns
- Unexpected additional columns

The validation test successfully confirmed that the sample input contained all required predictors and no additional or missing variables.

This reduces the risk of generating predictions from incorrectly structured input data.

---

## 10.4 Performance Rating Prediction

The prediction system generates one of the observed PerformanceRating categories:

- `2` — Good
- `3` — Excellent
- `4` — Outstanding

The XGBoost model internally uses encoded class labels during prediction. The prediction workflow maps these internal labels back to the original project PerformanceRating values.

The mapping used is:

| Internal Model Class | PerformanceRating |
|---:|---:|
| 0 | 2 |
| 1 | 3 |
| 2 | 4 |

This ensures that the prediction output remains consistent with the original dataset terminology.

---

## 10.5 Prediction Probabilities

In addition to the predicted PerformanceRating, the prediction system calculates the probability associated with each performance category.

For the sample employee used in the prediction notebook, the model produced:

| Performance Rating | Predicted Probability |
|---:|---:|
| 2 | 0.24% |
| 3 | 98.55% |
| 4 | 1.21% |

The predicted PerformanceRating for this sample employee was **Rating 3**.

The probability values provide additional information about the model's estimated class probabilities rather than only returning the predicted class.

---

## 10.6 Reusable Prediction Function

A reusable prediction function was implemented so that the model can be applied to new employee records without repeating the complete prediction procedure manually.

The function performs the following steps:

1. Receives employee input data.
2. Validates the required predictor variables.
3. Applies the saved preprocessing pipeline.
4. Generates the predicted performance rating.
5. Calculates prediction probabilities.
6. Returns the prediction and associated probabilities.

This provides a repeatable structure for future prediction requests.

---

## 10.7 Multiple Employee Prediction

The prediction workflow was also tested using multiple hypothetical employee records.

Two example employee records were passed through the prediction function.

Both examples received Rating 3 as the predicted PerformanceRating.

The associated probability distributions were:

| Employee | Rating 2 | Rating 3 | Rating 4 | Predicted Rating |
|---|---:|---:|---:|---:|
| Employee 1 | 0.24% | 98.55% | 1.21% | 3 |
| Employee 2 | 7.11% | 92.05% | 0.84% | 3 |

The second example had a higher estimated probability for Rating 2 than the first example, while Rating 3 remained the highest-probability class for both examples.

These examples demonstrate how the prediction system can process more than one employee record.

---

## 10.8 Prediction System Interpretation

The prediction notebook demonstrates that the saved model can successfully be restored and used to generate predictions for new employee records.

The system provides:

- PerformanceRating prediction
- Class probabilities
- Input validation
- Reusable prediction functionality
- Multiple-record prediction capability

The prediction probabilities should be interpreted as model-generated estimates rather than guarantees of future employee performance.

The prediction system is a demonstration of the trained model using the supplied project dataset. Additional validation would be required before using the system in an actual employee hiring or performance-management process.

---

## 10.9 Hiring Use-Case Limitation

The project requirement states that the trained model should be usable for predicting employee performance based on input factors and for supporting employee hiring.

However, some of the predictors used by the model describe an employee's existing workplace experience.

For example:

- `EmpEnvironmentSatisfaction`
- `EmpJobSatisfaction`
- `EmpWorkLifeBalance`
- `Attrition`
- `YearsWithCurrManager`
- `YearsSinceLastPromotion`

These variables may not be available for an external candidate before joining the organization.

Therefore, the current model demonstrates the required prediction workflow using the supplied employee dataset, but its direct use as a pre-hiring screening system would require a separate validation study and a feature set specifically designed around information available before hiring.

## 11. Results, Business Insights and Recommendations

The analysis combined exploratory data analysis, statistical testing, machine learning, feature-importance analysis, and prediction to address the business requirements of the project.

The major findings and recommendations are summarized below.

---

## 11.1 Major Results

The analysis identified several important patterns in employee performance.

### Performance Distribution

Rating 3 is the dominant performance category, representing 72.83% of employees.

Rating 2 represents 16.17% of employees, while Rating 4 represents 11.00%.

Therefore, the analysis considered the differences between all three performance categories rather than focusing only on the majority class.

### Department Differences

Performance distributions vary across departments.

Finance has the highest observed proportion of Rating 2 employees at 30.61%.

Development has the highest observed proportion of Rating 4 employees at 12.19%.

Department was also identified as a statistically significant categorical variable and ranked third in the tuned XGBoost feature-importance analysis.

### Job Role Differences

Job role was the most important feature in the tuned XGBoost model.

The distribution of performance ratings varies substantially across job roles, indicating that job role provides useful predictive information in the supplied dataset.

### Environment Satisfaction

Environment satisfaction showed a strong relationship with PerformanceRating.

Employees with satisfaction levels 1 and 2 had approximately 39–41% Rating 2 observations, while employees with levels 3 and 4 had less than 1% Rating 2 observations.

Environment satisfaction was also the second most important feature in the final XGBoost model.

### Salary Hike

Salary hike percentage was another important predictor.

It showed a statistically significant relationship with PerformanceRating and ranked fourth in the model-based feature-importance analysis.

Employees with Rating 4 had a higher average salary-hike percentage than the lower performance categories in the supplied dataset.

### Experience-related Variables

Several experience-related variables showed statistically significant differences across performance-rating groups.

These included:

- `YearsSinceLastPromotion`
- `ExperienceYearsInCurrentRole`
- `ExperienceYearsAtThisCompany`
- `YearsWithCurrManager`
- `TotalWorkExperienceInYears`

These variables therefore provide additional information about employee performance patterns.

---

## 11.2 Machine Learning Results

Eight classification algorithms were evaluated.

After baseline comparison and hyperparameter tuning, the final XGBoost model achieved:

- Accuracy: **93.75%**
- Balanced Accuracy: **87.04%**
- Macro Precision: **93.62%**
- Macro Recall: **87.04%**
- Macro F1: **90.03%**
- Tuned five-fold Cross-Validation Macro F1: **90.41%**

The final model successfully predicts the three performance-rating categories used in the dataset.

The class-wise F1-scores were:

- Rating 2: **0.86**
- Rating 3: **0.96**
- Rating 4: **0.88**

The model therefore demonstrates useful predictive performance on the supplied dataset, while minority-class performance should continue to be monitored when applying the model to new data.

---

## 11.3 Business Problem Mapping

The project requirements can be addressed as follows:

| Business Requirement | Analysis Outcome |
|---|---|
| Department-wise performance | Performance distributions were analyzed across all six departments |
| Identify important factors | Tuned XGBoost feature importance identified Job Role, Environment Satisfaction, and Department as the top three factors |
| Predict employee performance | A tuned XGBoost classification pipeline was trained and tested |
| Support hiring-related prediction | A reusable prediction workflow was developed for new employee records |
| Provide improvement recommendations | Recommendations were developed based on observed performance patterns and important predictive factors |

---

## 11.4 Recommendations for Improving Employee Performance

The following recommendations are based on the observed relationships in the dataset.

### 1. Monitor and Improve Workplace Environment

Environment satisfaction was one of the strongest observed predictors of PerformanceRating.

The organization can therefore consider:

- Regular employee feedback surveys
- Identification of workplace issues affecting satisfaction
- Department-level review of recurring employee concerns
- Manager discussions with employees experiencing lower workplace satisfaction
- Periodic monitoring of environment satisfaction trends

The objective should be to identify workplace factors associated with lower employee satisfaction and address them appropriately.

---

### 2. Review Performance Patterns by Job Role

Job role was the highest-ranked feature in the model-based feature-importance analysis.

The organization can analyze performance patterns within individual roles rather than applying identical performance-improvement approaches to every employee.

Possible actions include:

- Role-specific performance expectations
- Role-specific training
- Review of workload and responsibilities
- Identification of skill gaps
- Sharing effective practices between employees performing similar roles

---

### 3. Conduct Department-level Performance Reviews

Department was the third most important feature in the model.

Departments with higher observed proportions of lower performance ratings can be examined to understand differences in:

- Work environment
- Role distribution
- Workload
- Management practices
- Training opportunities
- Career progression
- Employee satisfaction

These reviews should focus on identifying organizational factors rather than attributing performance differences to individual employees without further evidence.

---

### 4. Review Career Progression and Promotion Patterns

`YearsSinceLastPromotion` showed a statistically significant relationship with PerformanceRating and was among the top five model-based features.

The organization can monitor whether employees experience prolonged periods without career progression and evaluate whether appropriate development opportunities are available.

Potential actions include:

- Career-development discussions
- Skill-development plans
- Internal mobility opportunities
- Clear promotion criteria
- Periodic review of employees approaching longer promotion intervals

---

### 5. Use Salary Hike Information Carefully

Salary hike percentage was an important predictive variable and showed a positive observed relationship with performance.

The organization can review compensation and performance-management processes together to understand whether compensation decisions are aligned with employee contribution and development.

The analysis does not establish that salary increases cause higher performance, so compensation decisions should not be based solely on the model.

---

### 6. Use Role-specific Training and Development

Several experience-related variables were associated with PerformanceRating.

Training and development programs can therefore be aligned with:

- Employee job role
- Current experience
- Career stage
- Identified skill gaps
- Future role requirements

This may allow development programs to be more targeted than applying the same training program to every employee.

---

## 11.5 Recommendations for Management

Based on the combined findings, management can establish a structured performance-improvement process:

1. Monitor department-level and role-level performance patterns.
2. Regularly measure workplace environment satisfaction.
3. Identify employees or groups showing lower satisfaction or performance patterns.
4. Conduct appropriate manager or HR discussions to understand underlying issues.
5. Provide role-specific development and training opportunities.
6. Review career progression and promotion processes.
7. Monitor compensation and salary-hike patterns alongside performance.
8. Re-evaluate performance trends periodically using updated employee data.

These actions are intended to support evidence-based performance management while avoiding conclusions about individual employees based solely on model predictions.

---

## 11.6 Important Business Considerations

The analysis identifies associations and predictive patterns rather than proving causal relationships.

For example, the model identifies environment satisfaction as an important predictor, but the analysis does not establish that increasing satisfaction by itself will necessarily increase PerformanceRating.

Similarly, differences between departments or job roles should not automatically be interpreted as evidence that one department or role causes better or worse employee performance.

Business decisions should therefore combine the analytical findings with organizational context, employee feedback, and appropriate management review.

---

## 11.7 Hiring-related Considerations

The project requirement includes using the trained model to support employee hiring.

However, the current dataset consists of existing employee records and includes variables that may only become available after an employee joins the organization.

Examples include:

- `EmpEnvironmentSatisfaction`
- `EmpJobSatisfaction`
- `EmpWorkLifeBalance`
- `Attrition`
- `YearsWithCurrManager`
- `YearsSinceLastPromotion`

Consequently, the current model demonstrates the required performance-prediction methodology but should not automatically be treated as a validated pre-hiring screening system.

A dedicated hiring model would require candidate-level data containing variables that are legitimately and consistently available before hiring.

---

## 11.8 Overall Project Outcome

The project provides an end-to-end analytical workflow for understanding and predicting employee performance.

The workflow includes:

- Data validation and preprocessing
- Exploratory data analysis
- Statistical significance testing
- Department-wise analysis
- Feature-importance analysis
- Multiple classification algorithms
- Cross-validation
- Hyperparameter tuning
- Final XGBoost model development
- Employee performance prediction
- Prediction probability estimation
- Visualization of important findings
- Business recommendations

The final model achieved a Macro F1 of **90.03%** on the held-out test set and **90.41%** in tuned five-fold cross-validation.

The analysis identifies job role, environment satisfaction, and department as the three highest-ranked predictive factors in the final model.

These findings provide a data-driven basis for understanding employee performance patterns and identifying areas for further organizational investigation.

## 12. Limitations and Conclusion

## 12.1 Project Limitations

The analysis provides useful insights into employee performance within the supplied INX Future Inc. dataset. However, several limitations should be considered when interpreting the results.

### Dataset Size

The dataset contains 1,200 employee records.

Although this is sufficient for the analysis and model-development exercise, a larger and more diverse employee dataset would provide additional evidence for validating the identified patterns.

### Target Class Imbalance

Performance Rating 3 represents 72.83% of the observations, while Ratings 2 and 4 represent smaller portions of the dataset.

Although stratified sampling, class-balanced training where applicable, and macro-level evaluation metrics were used, minority-class prediction remains an important consideration.

### Existing Employee Data

The dataset represents existing employees.

Several predictors describe an employee's current organizational experience and may not be available before hiring.

Examples include:

- `EmpEnvironmentSatisfaction`
- `EmpJobSatisfaction`
- `EmpWorkLifeBalance`
- `Attrition`
- `YearsWithCurrManager`
- `YearsSinceLastPromotion`

Therefore, the current model should be considered a performance-prediction demonstration based on the supplied dataset rather than a fully validated pre-hiring screening system.

### Feature Availability

The availability of certain variables may depend on the stage of the employee lifecycle.

A future hiring-specific model should use only information that is legitimately and consistently available during the hiring process.

### Predictive Association versus Causation

The statistical tests, correlations, and model-based feature importance identify relationships and predictive patterns.

They do not establish that a particular employee characteristic directly causes a change in performance.

For example, the importance of environment satisfaction in the model does not by itself prove that increasing satisfaction will cause higher performance.

### Model Generalization

The model was evaluated using the supplied dataset, an 80:20 stratified train-test split, and five-fold stratified cross-validation.

Although these procedures provide useful evidence of model performance, performance on future employees or employees from a different organization cannot be assumed to be identical.

Additional external or future-period validation would be required before operational deployment.

### Feature Importance Interpretation

The XGBoost feature-importance values describe the contribution of variables to the trained model's predictive process.

They should not be interpreted as causal effect sizes or as evidence that the highest-ranked variables are the only factors influencing employee performance.

---

## 12.2 Conclusion

This project analyzed employee performance data from INX Future Inc. using an end-to-end data science workflow.

The analysis began with data validation and preprocessing, followed by exploratory data analysis, statistical testing, correlation analysis, department-level analysis, and multivariate examination.

Multiple classification algorithms were then evaluated using a consistent train-test framework.

After cross-validation and hyperparameter tuning, XGBoost was selected as the final model.

The final model achieved:

- **93.75% Accuracy**
- **87.04% Balanced Accuracy**
- **93.62% Macro Precision**
- **87.04% Macro Recall**
- **90.03% Macro F1**
- **90.41% tuned five-fold Cross-Validation Macro F1**

The model-based feature-importance analysis identified the following three highest-ranked predictive factors:

1. `EmpJobRole`
2. `EmpEnvironmentSatisfaction`
3. `EmpDepartment`

Together, these three variables accounted for approximately 41.95% of the aggregated model-based feature importance.

The analysis also identified statistically significant relationships involving department, job role, overtime, environment satisfaction, salary hike percentage, and several experience-related variables.

The prediction notebook demonstrated that the saved model can be loaded and used to predict PerformanceRating for new employee records while also providing class probabilities and input validation.

From a business perspective, the findings provide areas for further investigation, including workplace environment, role-specific performance patterns, department-level differences, career progression, and compensation practices.

The recommendations are intended to support data-informed investigation and performance-improvement planning. They should be combined with organizational context, employee feedback, and appropriate management processes rather than being treated as automatic decisions based solely on model output.

Overall, the project demonstrates a complete data science workflow for analyzing employee performance and developing a machine learning-based performance prediction system using the supplied INX Future Inc. dataset.