# Exercise 5.2A: Simple ML Pipeline Tutorial

**Complete Beginner-Friendly Hands-On Tutorial**

---

## 📚 Contents

This folder contains all materials for the simplified Exercise 5.2A - a complete, self-contained ML pipeline tutorial perfect for teaching assistants and beginner students.

### Files

1. **`simple_pipeline_tutorial.ipynb`** - Main tutorial notebook
   - 11 steps covering complete ML pipeline
   - Self-contained with synthetic data generation
   - Detailed markdown explanations
   - Includes 4 practice challenges

2. **`SIMPLE_PIPELINE_TUTORIAL.md`** - Teaching Assistant guide
   - 90-minute session structure
   - Key concepts to emphasize
   - Common student mistakes
   - Assessment rubric
   - Troubleshooting guide

3. **`TUTORIAL_SUMMARY.md`** - Quick reference
   - Visual overview
   - Expected results
   - Integration with course

4. **`requirements_simple_tutorial.txt`** - Python dependencies
   - All required packages
   - Version specifications

---

## 🚀 Quick Start

### For Students

```powershell
# Navigate to this folder
cd 5.2A_Simple_Pipeline

# Create virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements_simple_tutorial.txt

# Launch Jupyter
jupyter notebook simple_pipeline_tutorial.ipynb
```

### For Teaching Assistants

1. Review **`SIMPLE_PIPELINE_TUTORIAL.md`** for session structure
2. Run through the notebook yourself first
3. Prepare talking points for key concepts
4. Have the **`TUTORIAL_SUMMARY.md`** open for reference during session

---

## 🎯 What Students Will Learn

✅ Complete ML pipeline workflow  
✅ Handling class imbalance (SMOTE)  
✅ Proper train/test splitting  
✅ Security-specific metrics (TPR, FPR, precision)  
✅ Confusion matrix interpretation  
✅ ROC curve analysis  
✅ Feature importance  
✅ Model deployment preparation  

**Duration:** 60-90 minutes  
**Difficulty:** Beginner  
**Prerequisites:** Basic Python, pandas, scikit-learn

---

## 📖 Scenario

Build an email phishing detection system for enterprise email security:
- 10,000 emails processed per day
- ~10% phishing emails (realistic imbalance)
- False positives frustrate users
- False negatives enable credential theft

---

## 📊 Expected Results

With default parameters:
- **ROC-AUC:** 0.90-0.95
- **Precision:** 0.75-0.85
- **Recall (TPR):** 0.85-0.95
- **FPR:** 0.02-0.05

---

## 🔗 Related Exercises

**Prerequisites:**
- Chapter 4: Feature Engineering basics

**Follow-Up:**
- Exercise 5.4A: ROC & Youden Index (`../youden_demo/02_roc_youden_threshold.ipynb`)
- Exercise 5.4B: Cost-Weighted Optimization (`../youden_demo/03_cost_weighted_tuning.ipynb`)

---

## 💡 Key Features

✅ **No External Data** - Generates synthetic email dataset  
✅ **Self-Explanatory** - Detailed explanations in each cell  
✅ **Realistic Context** - Email security operational scenarios  
✅ **Visual Learning** - Plots and visualizations  
✅ **Practice Challenges** - 4 extension activities  

---

## 📝 Assessment

Optional grading rubric (100 points):
- Notebook completion: 30 points
- Understanding: 40 points
- Challenges completed: 20 points
- Documentation: 10 points

---

## 🐛 Troubleshooting

**Import Error:**
```powershell
pip install imbalanced-learn
```

**Plots not showing:**
Add to first cell: `%matplotlib inline`

**Kernel crashes:**
Reduce `n_samples` in Step 2 data generation

---

## 📧 Support

- Review Chapter 5, Section 5.2
- Check main Exercises README: `../README.md`
- Contact course instructor or TA

---

**Version:** 1.0  
**Created:** November 25, 2025  
**Exercise:** 5.2A (Simplified Version)  
**Module:** 3, Chapter 5 - ML Algorithm Development Pipeline
