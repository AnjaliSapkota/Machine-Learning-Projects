# Sonar Rock vs Mine Classification using Machine Learning

A machine learning project that classifies sonar signals as either **Rock (R)** or **Mine (M)** using **Logistic Regression**. The project includes data preprocessing, exploratory data analysis (EDA), model training, evaluation, and prediction.

## Overview

The Sonar dataset consists of sonar signals reflected from different objects. Each sample contains **60 numerical features** representing energy values at different frequencies, with a target label indicating whether the object is a **Rock (R)** or a **Mine (M)**.

This project demonstrates a complete binary classification workflow using Python and Scikit-learn.

---

## Features

- Load and inspect the Sonar dataset
- Exploratory Data Analysis (EDA)
- Summary statistics
- Missing value and duplicate check
- Target class distribution visualization
- Correlation heatmap
- Feature boxplots for outlier detection
- Train-test data split
- Logistic Regression model training
- Model evaluation using accuracy
- Prediction on new sonar readings

---

## Dataset

- **Instances:** 208
- **Features:** 60 numeric attributes
- **Target Classes:**
  - `R` – Rock
  - `M` – Mine

Dataset Source:
- Kaggle
--- https://www.kaggle.com/datasets/aryansingh2000/sonar-data-set?resource=download


---

## Machine Learning Pipeline

1. Load dataset
2. Separate features and target variable
3. Split data into training and testing sets
4. Train Logistic Regression classifier
5. Evaluate model performance
6. Predict unseen samples

---

## Model Performance

Training Accuracy

```
83.42%
```

Testing Accuracy

```
76.19%
```

## License

This project is open-source and available under the MIT License.
