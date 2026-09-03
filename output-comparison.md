# Output Comparison

This file documents the changes in model output as new features and improvements were added to the prototype.

---

## Output 1

**Model version:** Initial prototype

**Features:** 4 basic features

* House size
* Number of bedrooms
* Number of floors
* House age

**Limitations at this stage:**

* No feature scaling
* No feature engineering
* Very small dataset
* No train/test split or proper model evaluation

### Output

<img width="948" height="278" alt="Output 1" src="https://github.com/user-attachments/assets/93145510-f531-43f2-b3fe-e624657f4b6d" />

---

## Output 2

**Model version:** Feature-scaled model

**Changes:**

* Added Z-score feature normalization.
* Increased the dataset from 3 training examples to 20.
* The model still uses the original 4 features.

**Purpose:**

Feature scaling puts the features on a more comparable scale, allowing gradient descent to converge more effectively.

### Output

<img width="973" height="648" alt="Output 2" src="https://github.com/user-attachments/assets/86728f1a-4298-44dc-8ad9-d1622e2fed4b" />

---

## Output 3

**Model version:** Feature-engineered model

**Changes:**

* Added feature engineering.
* Increased the number of features from **4 to 9**.
* Added polynomial features:

  * `size²`
  * `age²`
* Added interaction features:

  * `size × bedrooms`
  * `size × floors`
  * `size × age`
* Continued using Z-score normalization.
* Updated the prediction pipeline to automatically generate the engineered features from user input.

### Output

<img width="1076" height="696" alt="Output 3" src="https://github.com/user-attachments/assets/1533cca9-426c-4c10-bd42-ac19eff6dd84" />

---


The outputs demonstrate how the model evolved from a basic linear regression prototype into a more expressive model with feature scaling and engineered polynomial and interaction features.

> **Note:** Changes in predicted values do not necessarily mean that the newer model is more accurate. Proper evaluation on unseen test data is required to determine whether each modification actually improves model performance.
