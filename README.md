# Employee Performance Analysis & Prediction API

### INX Future Inc. | Certified Data Scientist Project

An end-to-end data science project focused on analyzing employee performance and building a machine learning model to predict employee performance ratings. The project combines exploratory data analysis, data preprocessing, model development, evaluation, and a containerized prediction API built with **FastAPI and Docker**.

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn\&logoColor=white)](https://scikit-learn.org/)
[![XGBoost](https://img.shields.io/badge/XGBoost-Model-red)](https://xgboost.readthedocs.io/)
[![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi\&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker\&logoColor=white)](https://www.docker.com/)

---

## Project Overview

Employee performance is influenced by several workplace and individual factors. Understanding how these factors relate to performance can help an organization explore workforce patterns and support data-informed HR analysis.

This project uses employee data from the fictional company **INX Future Inc.** to:

* Explore employee characteristics and performance patterns.
* Clean and prepare the dataset for machine learning.
* Train and evaluate classification models.
* Select and tune an XGBoost model.
* Build an API that accepts employee information and returns a predicted performance rating with class probabilities.
* Package the API and trained model into a Docker container.

**Project type:** Supervised Machine Learning — Multiclass Classification
**Target variable:** `PerformanceRating`
**Target classes:** 2, 3, and 4

---

## Results

The final tuned XGBoost model was evaluated on a held-out test set.

| Metric                       |     Result |
| ---------------------------- | ---------: |
| Test Accuracy                | **93.75%** |
| Balanced Accuracy            | **87.04%** |
| Macro F1-score               | **90.03%** |
| Best Tuned CV Macro F1-score | **90.41%** |

The model predicts one of three employee performance ratings: **2, 3, or 4**.

These are results from this project's evaluation data; they do not guarantee the same performance on new employees or in another organization.

---

## Tech Stack

| Area              | Tools                                  |
| ----------------- | -------------------------------------- |
| Programming       | Python                                 |
| Data analysis     | Pandas, NumPy                          |
| Visualization     | Matplotlib and notebook-based analysis |
| Machine learning  | Scikit-learn, XGBoost                  |
| Model persistence | Joblib                                 |
| API development   | FastAPI, Pydantic                      |
| API server        | Uvicorn                                |
| Containerization  | Docker                                 |
| Development       | Jupyter Notebook, VS Code              |
| Version control   | Git, GitHub                            |
| Cloud deployment  | AWS EC2 — planned                      |

---

## Project Workflow

1. **Data understanding and exploratory analysis**
   Examine the employee dataset, understand its variables, inspect distributions, and explore patterns relevant to performance.

2. **Data processing**
   Prepare the data for modeling, handle data quality issues, and organize the features for the machine learning workflow.

3. **Model development**
   Train classification models and evaluate their predictive performance.

4. **Model selection and tuning**
   Tune the XGBoost model and evaluate it using classification metrics, including macro F1-score and balanced accuracy.

5. **Prediction pipeline**
   Save the trained preprocessing and prediction pipeline using Joblib.

6. **API development**
   Build a FastAPI application with a health endpoint and a prediction endpoint. Validate incoming employee records using Pydantic.

7. **Dockerization**
   Package the API, dependencies, and trained model into a Docker image and run it as a container.

8. **Cloud deployment**
   AWS EC2 deployment is the next planned stage.

---

## Repository Structure

```text
INX-Future-Employee-Performance/
│
├── api/
│   ├── main.py
│   └── schemas.py
│
├── models/
│   └── final_xgboost_employee_performance_model.joblib
│
├── src/
│   ├── Data Processing/
│   │   ├── data_exploratory_analysis.ipynb
│   │   └── data_processing.ipynb
│   │
│   ├── models/
│   │   ├── train_model.ipynb
│   │   └── predict_model.ipynb
│   │
│   └── visualization/
│       └── visualize.ipynb
│
├── Project Summary/
│   ├── Analysis/
│   │   └── project_analysis.md
│   ├── Requirement/
│   │   └── project_requirement.md
│   └── Summary/
│       └── project_summary.md
│
├── .dockerignore
├── .gitignore
├── Dockerfile
└── requirements.txt
```

The raw and processed datasets and the reference PDFs are not included in this repository at present.

---

## Run the API Locally

### 1. Clone the repository

```bash
git clone https://github.com/asishmohantychandan/INX-Future-Employee-Performance.git
cd INX-Future-Employee-Performance
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Start the API

From the project root:

```bash
python -m uvicorn main:app --app-dir api --reload
```

The API will be available at:

* API base: `http://127.0.0.1:8000`
* Interactive documentation: `http://127.0.0.1:8000/docs`
* Health check: `http://127.0.0.1:8000/health`

---

## API Endpoints

### `GET /health`

Checks whether the API is running and whether the model has loaded.

Example response:

```json
{
  "status": "healthy",
  "model_loaded": true
}
```

### `POST /predict`

Accepts an employee record and returns a predicted performance rating and probabilities for the three classes.

The request schema expects **26 input features**, covering employee demographics, work experience, job information, satisfaction, and employment-related attributes. See `api/schemas.py` for the exact field names and data types.

Example response:

```json
{
  "predicted_performance_rating": 3,
  "probabilities": {
    "2": 0.002398,
    "3": 0.983896,
    "4": 0.013706
  }
}
```

The values above illustrate a successful local API test. Submit a complete request body matching the schema through `/docs` to test your own prediction.

---

## Run with Docker

Docker lets you run the API and model in a container without launching the application directly from your local Python environment.

### 1. Build the image

From the repository root:

```bash
docker build -t inx-employee-api:1.0 .
```

### 2. Start the container

```bash
docker run -d \
  --name inx-employee-container \
  -p 8001:8000 \
  inx-employee-api:1.0
```

For Windows PowerShell, the same command can be run on one line:

```powershell
docker run -d --name inx-employee-container -p 8001:8000 inx-employee-api:1.0
```

### 3. Verify the container

```bash
docker ps
```

Check the container logs if needed:

```bash
docker logs inx-employee-container
```

Open:

* Health check: `http://127.0.0.1:8001/health`
* API documentation: `http://127.0.0.1:8001/docs`

**Local Docker testing:** The container was built and started successfully, and the health and prediction endpoints were tested.

### 4. Stop the container

```bash
docker stop inx-employee-container
```

To remove it after stopping:

```bash
docker rm inx-employee-container
```

---

## Model and Feature Notes

* **Problem type:** Multiclass classification.
* **Target:** `PerformanceRating`.
* **Classes:** 2, 3, and 4.
* **Final estimator:** Tuned XGBoost classifier within the saved prediction pipeline.
* **Model file:** `models/final_xgboost_employee_performance_model.joblib`.
* **Preprocessing:** Packaged with the trained pipeline so the API can apply the same transformations at prediction time.
* **Input validation:** Pydantic schema rejects missing required fields and unexpected extra fields.

The API maps the model's internal class encoding back to the original performance-rating labels before returning the response.

**Important modeling consideration:** Some predictors, such as `Attrition` and employee satisfaction measures, may not be available or appropriate at every point when an organization would want to make a prediction. Their use should be considered in relation to the intended prediction timing and business process. This model is an analytical project, not a validated HR decision system.

---

## Data

The project uses the INX Future Inc. employee performance dataset associated with the Certified Data Scientist project.

The source and processed data files are kept outside this public repository for now. To reproduce the analysis, obtain the dataset through the authorized project materials and place the files in the expected local data folders, then follow the notebooks in `src/`.

The repository does not currently provide an automated data-download script.

---

## Limitations

* The reported metrics are based on the project's evaluation split and may not represent performance on data from another time period, company, or employee population.
* Class-level performance and potential class imbalance should be considered alongside overall accuracy.
* The dataset represents a specific project scenario and may not reflect the full complexity of real organizational performance.
* Predictions should not be used as the sole basis for employee evaluation, promotion, compensation, or other consequential HR decisions.
* AWS deployment and production monitoring are not yet completed.

---

## Future Improvements

* Deploy the container on AWS EC2 and verify the public endpoint.
* Add automated API tests and model input validation tests.
* Add structured logging and safer error handling.
* Add CI/CD automation for testing and deployment.
* Add monitoring for API availability, prediction behavior, and model performance.
* Document reproducible data acquisition and model retraining steps.

---

## Author

**Asish Mohanty Chandan**
B.Tech — Information Science & Engineering

* GitHub: [asishmohantychandan](https://github.com/asishmohantychandan)
* LinkedIn: [Asish Mohanty](https://www.linkedin.com/in/asish-mohanty44/)

---

## Acknowledgment

This project was completed as part of the **IABAC Certified Data Scientist** project work, using the INX Future Inc. employee performance analysis scenario.
