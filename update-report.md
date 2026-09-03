# Update Report

## Update 1

**Date:** September 2, 2026
**Time:** 16:15 GMT+5:45

**Changes:**

* Added feature scaling to the model using Z-score normalization.

---

## Update 2

**Date:** September 3, 2026
**Time:** 13: 30 GMT+5:45

**Changes:**

* Added feature engineering to the model.
* Added polynomial features including `size²` and `age²`.
* Added interaction features including `size × bedrooms`, `size × floors`, and `size × age`.
* Updated the prediction pipeline to automatically generate engineered features from user-provided input.
