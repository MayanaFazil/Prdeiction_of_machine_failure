# 🔧 Machine Failure Prediction using Machine Learning

## 📌 Overview

This project focuses on predicting machine failure using historical sensor and operational data. It applies supervised machine learning techniques to classify whether a machine is likely to fail. The objective is to enable predictive maintenance, reduce unplanned downtime, and enhance system reliability.

---

## 📊 Problem Statement

Industrial equipment can unexpectedly fail, leading to costly repairs and halted production. By analyzing key features like temperature, torque, and rotational speed, we aim to build a model that:
- Predicts machine failures in advance
- Improves preventive maintenance scheduling
- Minimizes overall maintenance costs and downtime

---

## 📁 Dataset Description

The dataset includes the following features:
- `Air temperature [K]`
- `Process temperature [K]`
- `Rotational speed [rpm]`
- `Torque [Nm]`
- `Tool wear [min]`
- `Failure Type` (binary: 0 = No Failure, 1 = Failure)

---

## 🧠 Machine Learning Approach

### Steps Followed:
1. **Data Loading & Cleaning**
2. **Exploratory Data Analysis (EDA)**
3. **Feature Engineering**
4. **Model Building & Evaluation**
5. **Performance Comparison**
6. **Visualization of Results**

### 🧪 Algorithms Used:
- ✅ **Naive Bayes Classifier**  
- 🌲 **Random Forest Classifier**  
- 🚀 **Gradient Boosting Classifier**

### 📏 Evaluation Metrics:
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- Confusion Matrix  

---

## 📈 Results

Among the tested models:
- **Gradient Boosting Classifier** achieved the highest accuracy and precision.
- Feature importance plots highlighted the key contributors to failure.
- Naive Bayes performed well for baseline comparison due to its simplicity and speed.

---

## 🛠️ Tech Stack

- **Languages & Tools**: Python, Jupyter Notebook
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn
- **ML Techniques**: Supervised Learning, Classification, Feature Importance

---
