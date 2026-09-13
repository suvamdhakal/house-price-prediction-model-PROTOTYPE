# Update Report

## Update 1

**Date:** September 2, 2026

**Time:** 16:15 GMT+5:45

**Changes:**

* Added feature scaling to the model using Z-score normalization.

---

## Update 2

**Date:** September 3, 2026

**Time:** 13:30 GMT+5:45

**Changes:**

* Added feature engineering to the model.
* Added polynomial features including `size²` and `age²`.
* Added interaction features including `size × bedrooms`, `size × floors`, and `size × age`.
* Updated the prediction pipeline to automatically generate engineered features from user-provided input.

---

## Update 3

**Date:** September 14, 2026

**Time:** 19:00 GMT+5:45

**Changes:**

* Added L2 regularization to the model.
* Updated the cost function to include the L2 regularization term.
* Updated the gradient calculation to include the regularization term for the model weights.
* The bias term is not regularized.
* Added a regularization parameter (`Lambda`) to control the strength of regularization.
