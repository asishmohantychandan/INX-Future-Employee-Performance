# Employee Performance Analysis
## Project Summary

## 1. Executive Summary

INX Future Inc. is experiencing concerns related to employee performance, increasing escalations, and a decline in client satisfaction.

This project analyzes employee-level data to identify important factors associated with PerformanceRating, understand department-wise performance patterns, develop a machine learning model for performance prediction, and provide recommendations for improving employee performance.

The project follows an end-to-end data science workflow consisting of data validation, preprocessing, exploratory data analysis, statistical testing, machine learning model development, model comparison, hyperparameter tuning, feature-importance analysis, prediction, and visualization.

The dataset contains **1,200 employee records** and **28 variables** in the original source data.

The observed PerformanceRating categories are:

- Rating 2 — Good
- Rating 3 — Excellent
- Rating 4 — Outstanding

Rating 3 is the majority category, representing **72.83%** of employees.

---

## 2. Business Objectives

The project addresses the following business objectives:

1. Analyze employee performance across departments.
2. Identify the most important factors associated with employee performance.
3. Develop a machine learning model capable of predicting employee PerformanceRating.
4. Demonstrate prediction for new employee records.
5. Provide data-driven recommendations for improving employee performance.

---

## 3. Data and Analytical Approach

The supplied employee dataset was validated for missing values, duplicate records, categorical consistency, target-value validity, and logical consistency among experience-related variables.

No employee records were removed during preprocessing.

`EmpNumber` was excluded from machine learning because it is an employee identifier.

The remaining **26 predictor variables** were classified as:

- Ordinal variables
- Nominal categorical variables
- Numerical variables

Categorical variables were one-hot encoded, while numerical and ordinal variables were standardized for models requiring scaled inputs.

The data was divided using an **80:20 stratified train-test split**, resulting in:

- 960 training records
- 240 testing records

Multiple classification algorithms were evaluated using consistent training and testing data.

---

## 4. Exploratory Analysis Findings

The exploratory analysis identified several important relationships with employee performance.

### Department-wise Performance

Performance Rating 3 is the dominant category across all departments.

The observed Rating 2 proportions were:

- Data Science: 5.00%
- Development: 3.60%
- Finance: 30.61%
- HR: 18.52%
- R&D: 19.83%
- Sales: 23.32%

Finance had the highest observed proportion of Rating 2 employees, while Development had the highest observed proportion of Rating 4 employees at 12.19%.

### Statistical Findings

Chi-square testing identified statistically significant associations between PerformanceRating and:

- `EmpDepartment`
- `EmpJobRole`
- `OverTime`

Kruskal-Wallis testing identified statistically significant differences for several variables, including:

- `EmpEnvironmentSatisfaction`
- `EmpLastSalaryHikePercent`
- `YearsSinceLastPromotion`
- `ExperienceYearsInCurrentRole`
- `EmpWorkLifeBalance`
- `YearsWithCurrManager`
- `ExperienceYearsAtThisCompany`
- `EmpJobLevel`
- `TotalWorkExperienceInYears`

---

## 5. Top Three Predictive Factors

The tuned XGBoost model identified the following three highest-ranked predictive factors:

1. `EmpJobRole`
2. `EmpEnvironmentSatisfaction`
3. `EmpDepartment`

Their aggregated model-based feature importance was:

| Rank | Feature | Importance |
|---:|---|---:|
| 1 | `EmpJobRole` | 16.03% |
| 2 | `EmpEnvironmentSatisfaction` | 13.79% |
| 3 | `EmpDepartment` | 12.13% |

Together, these three features accounted for approximately **41.95%** of the aggregated model-based feature importance.

### Job Role

Performance distributions varied considerably across job roles, making `EmpJobRole` the highest-ranked predictive feature.

### Environment Satisfaction

Environment satisfaction showed a strong relationship with performance.

Rating 2 represented:

- 39.13% of employees with satisfaction level 1
- 40.50% of employees with satisfaction level 2
- 0.82% of employees with satisfaction level 3
- 0.83% of employees with satisfaction level 4

This variable was also statistically significant with p-value < 0.0001.

### Department

Department showed significant differences in performance distributions and was the third-ranked predictive feature.

The chi-square test produced a p-value < 0.0001 for the relationship between department and PerformanceRating.

These factors represent predictive relationships in the supplied dataset and should not be interpreted as proven causal factors.

---

## 6. Machine Learning Results

Eight classification algorithms were evaluated.

The leading models were further tuned using GridSearchCV with five-fold cross-validation and Macro F1 as the optimization metric.

The final tuned model comparison was:

| Model | Accuracy | Balanced Accuracy | Macro F1 |
|---|---:|---:|---:|
| XGBoost | 93.75% | 87.04% | 90.03% |
| Gradient Boosting | 93.33% | 87.51% | 89.66% |
| Random Forest | 92.50% | 84.95% | 87.64% |

The final XGBoost model achieved:

- **Accuracy: 93.75%**
- **Balanced Accuracy: 87.04%**
- **Macro Precision: 93.62%**
- **Macro Recall: 87.04%**
- **Macro F1: 90.03%**
- **Tuned five-fold Cross-Validation Macro F1: 90.41%**

Class-wise F1-scores were:

| Performance Rating | F1-Score |
|---:|---:|
| 2 | 0.86 |
| 3 | 0.96 |
| 4 | 0.88 |

The complete tuned XGBoost preprocessing and model pipeline was saved for subsequent prediction.

---

## 7. Prediction System

A separate prediction workflow was developed using the saved model.

The system:

- Loads the trained model pipeline.
- Accepts the 26 required predictor variables.
- Validates the input structure.
- Predicts PerformanceRating.
- Generates class probabilities.
- Supports multiple employee records.

For the sample employee used in the prediction notebook, the model predicted:

**PerformanceRating: 3**

with estimated probabilities of:

- Rating 2: 0.24%
- Rating 3: 98.55%
- Rating 4: 1.21%

The prediction output represents a model estimate and should not be interpreted as a guaranteed employee outcome.

---

## 8. Business Recommendations

Based on the observed patterns, the following actions can be considered by management.

### Workplace Environment

Regularly monitor employee environment satisfaction and investigate workplace factors associated with lower satisfaction.

### Job Role Analysis

Review performance patterns within individual job roles and consider role-specific expectations, development plans, and skill-gap analysis.

### Department-level Review

Analyze departments with higher observed proportions of lower performance ratings to identify differences in workload, management practices, employee satisfaction, development opportunities, and career progression.

### Career Development

Review promotion and career-development patterns, particularly for employees experiencing longer periods without promotion.

### Compensation Review

Review salary-hike and performance patterns together as part of the organization's compensation and performance-management processes.

### Targeted Development

Use employee role, experience, and identified skill gaps to design more targeted training and development programs.

These recommendations are based on observed relationships in the dataset and should be combined with employee feedback and organizational context.

---

## 9. Key Business Insight

The analysis indicates that employee performance is associated with a combination of role, workplace environment, department, compensation-related variables, and experience-related variables.

The three highest-ranked predictive factors in the final model are:

**Job Role → Environment Satisfaction → Department**

This suggests that employee performance analysis should consider organizational and role-specific context rather than relying on a single employee attribute.

---

## 10. Limitations

The model was developed using the supplied dataset of existing employees.

Some predictors used by the model, such as environment satisfaction, work-life balance, attrition, and manager-related experience, may not be available before an external candidate joins the organization.

Therefore, the current model demonstrates the performance-prediction methodology but should not automatically be considered a validated pre-hiring screening system.

A dedicated hiring model would require candidate-level data containing variables that are available and appropriate before hiring.

In addition, statistical relationships and model-based feature importance indicate associations and predictive usefulness rather than causation.

Further validation using future or external employee data would be required before operational deployment.

---

## 11. Conclusion

The project successfully developed an end-to-end employee performance analysis and prediction workflow for INX Future Inc.

The analysis identified meaningful differences in employee performance across departments and job roles and highlighted environment satisfaction, salary hike percentage, and several experience-related variables as important analytical factors.

The tuned XGBoost model achieved a **90.03% Macro F1 score on the held-out test set** and **90.41% Macro F1 in tuned five-fold cross-validation**.

The model-based analysis identified:

1. `EmpJobRole`
2. `EmpEnvironmentSatisfaction`
3. `EmpDepartment`

as the three highest-ranked predictive factors.

The project also provides a reusable prediction workflow that validates new employee inputs and produces both predicted PerformanceRating and class probabilities.

Overall, the analysis provides a data-driven framework for understanding employee performance patterns, supporting further investigation, and identifying areas for employee development and organizational improvement.