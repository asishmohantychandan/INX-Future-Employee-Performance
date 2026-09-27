# Employee Performance Analysis
## Project Requirement

### 1. Business Background

INX Future Inc. is a leading data analytics and automation solutions provider with more than 15 years of global business presence.

In recent years, the employee performance indexes have become a growing concern for the management. Service delivery escalations have increased, while client satisfaction levels have decreased by 8 percentage points.

The management wants to understand the underlying factors associated with employee performance and identify appropriate actions without negatively affecting overall employee morale.

### 2. Business Objective

The objective of this project is to analyze the available employee data and identify the factors associated with employee performance.

The analysis should provide useful information to management for understanding performance differences across departments, identifying important predictive factors, and supporting employee-related decisions.

### 3. Expected Project Insights

The project brief specifies the following four expected insights:

1. **Department-wise Performance**

   Analyze employee performance across different departments and identify differences in the distribution of performance ratings.

2. **Top 3 Important Factors Affecting Employee Performance**

   Identify the three most important factors associated with employee performance using appropriate analytical and machine learning techniques.

3. **Employee Performance Prediction Model**

   Develop a trained machine learning model that predicts employee PerformanceRating using employee-related factors as inputs.

   The project brief states that the model is intended to support employee hiring decisions.

4. **Recommendations to Improve Employee Performance**

   Provide recommendations based on the findings from exploratory analysis, statistical analysis, feature importance analysis, and machine learning results.

### 4. Project Dataset

The project uses the employee performance dataset provided with the IABAC Certified Data Scientist project.

The dataset contains employee-level information covering demographic, educational, job-related, satisfaction, experience, compensation, work-life balance, and other employee attributes.

The target variable for this project is:

`PerformanceRating`

The observed target values in the supplied dataset are:

- `2`
- `3`
- `4`

### 5. Project Deliverables

The project should contain:

- Data processing and preparation
- Exploratory data analysis
- Feature analysis and selection
- Machine learning model development
- Model evaluation and comparison
- Final model selection
- Employee performance prediction
- Visualizations
- Business insights
- Recommendations
- Project summary and analysis documentation

### 6. Submission Structure

The project follows the directory structure specified in the IABAC project submission guidelines:

```text
Project Summary/
├── Requirement/
├── Analysis/
└── Summary/

data/
├── external/
├── processed/
└── raw/

src/
├── Data Processing/
│   ├── data_processing.ipynb
│   └── data_exploratory_analysis.ipynb
├── models/
│   ├── train_model.ipynb
│   └── predict_model.ipynb
└── visualization/
    └── visualize.ipynb

references/