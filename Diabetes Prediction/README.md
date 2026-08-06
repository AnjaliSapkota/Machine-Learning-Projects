# 🩺 Diabetes Prediction using Support Vector Machine (SVM)

A Machine Learning project that predicts whether a person is diabetic based on medical diagnostic measurements using a **Support Vector Machine (SVM)** classifier.

---

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help in timely diagnosis and treatment.

This project uses dataset from kaggle to build a binary classification model that predicts whether a patient has diabetes based on health-related attributes.

The project includes:

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Standardization
- Model Training using SVM
- Model Evaluation
- Prediction on New Patient Data

---

## 📊 Exploratory Data Analysis

The following analyses were performed:

- Dataset overview
- Statistical summary
- Missing value check
- Duplicate value check
- Correlation Heatmap
- Diabetes Outcome Distribution
- Class-wise Feature Analysis

### Key Findings

- Dataset contains **768 records**.
- No missing values.
- No duplicate records.
- Target classes:
  - **500 Non-Diabetic**
  - **268 Diabetic**
- Glucose, BMI, Age, and Pregnancies show stronger relationships with diabetes compared to other features.

---

## ⚙️ Data Preprocessing

The preprocessing pipeline includes:

- Separating features and target
- Standardizing numerical features using **StandardScaler**
- Splitting dataset into:
  - **80% Training**
  - **20% Testing**
- Stratified train-test split for balanced class distribution

---

## 🤖 Machine Learning Model

Algorithm used:

- **Support Vector Machine (SVM)**
- Kernel: **Linear**

```python
classifier = svm.SVC(kernel='linear')
```

---

## 📈 Model Performance

| Metric | Score |
|---------|-------|
| Training Accuracy | **78.66%** |
| Testing Accuracy | **77.27%** |

The model performs consistently on both training and testing data, indicating reasonable generalization with minimal overfitting.

---

## 🔍 Prediction Example

Input:

```python
(5,166,72,19,175,25.8,0.587,51)
```

Prediction:

```
The person is diabetic
```

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Google Colab

---

## 📚 Learning Outcomes

Through this project, I learned:

- Data preprocessing techniques
- Exploratory Data Analysis (EDA)
- Feature scaling using StandardScaler
- Training an SVM classifier
- Evaluating classification models
- Making predictions using trained machine learning models

---


## 📄 License

This project is licensed under the MIT License.

Feel free to use, modify, and share this project for educational purposes.
