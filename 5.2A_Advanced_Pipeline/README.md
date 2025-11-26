# Exercise 5.2A.1: Advanced ML Pipeline Tutorial

**Production ML Lifecycle with Continuous Improvement Cycle**

---

## 📚 Contents

This folder contains materials for Exercise 5.2A.1 - an advanced ML pipeline tutorial demonstrating the complete **continuous improvement cycle** for security ML models in production.

### Files

1. **`advanced_pipeline_tutorial.ipynb`** - Main tutorial notebook
   - 17 comprehensive steps across 6 phases
   - Production deployment simulation
   - Concept drift detection
   - Automated retraining pipeline
   - A/B testing framework
   - Practice challenges

2. **`IMPLEMENTATION_PLAN.md`** - Detailed technical specification
   - Complete step-by-step breakdown
   - Data structures and algorithms
   - Expected results and metrics
   - Integration with ML_PIPELINE_FLOW.md

3. **`requirements_advanced_tutorial.txt`** - Python dependencies
   - All required packages with versions
   - Additional libraries for drift detection

4. **`generate_notebook.py`** - Notebook generation helper
   - Script to rebuild notebook from scratch
   - Useful for customization

---

## 🎯 Learning Objectives

After completing this tutorial, you will be able to:

✅ **Deploy ML Models to Production**
- Implement production scoring functions
- Handle real-time prediction requests
- Log predictions and features for monitoring

✅ **Monitor Model Performance**
- Track TPR, FPR, Precision over time
- Create monitoring dashboards
- Set alert thresholds for degradation

✅ **Detect Concept Drift**
- Apply statistical tests (Kolmogorov-Smirnov)
- Monitor feature distribution changes
- Identify performance degradation patterns

✅ **Implement Feedback Loops**
- Collect analyst corrections (TP/FP labels)
- Aggregate feedback for retraining
- Prioritize high-value labeling

✅ **Execute Automated Retraining**
- Trigger retraining on drift/performance thresholds
- Re-engineer features on updated data
- Validate retrained models on recent data

✅ **Perform A/B Testing**
- Deploy multiple model versions simultaneously
- Compare performance statistically (McNemar's test)
- Make data-driven deployment decisions

✅ **Implement Gradual Rollouts**
- Canary deployments (10% → 50% → 100%)
- Monitor for regressions
- Rollback capability

---

## 🚀 Quick Start

### Prerequisites

**Required:**
- ✅ Complete Exercise 5.2A (Simple Pipeline) first!
- Python 3.8+
- Jupyter Notebook or JupyterLab
- Basic understanding of ML workflows

**Recommended:**
- Read Chapter 6, Section 6.3 (Long-Term Maintenance)
- Review ML_PIPELINE_FLOW.md (Continuous Improvement Cycle section)

### Installation

```powershell
# Navigate to this folder
cd "C:\Users\BITS\Desktop\aiml-sec\content\modules\Module_03_Data_Science_ML_Foundations\Chapter5\Exercises\5.2A_Advanced_Pipeline"

# Create virtual environment (recommended)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements_advanced_tutorial.txt

# Launch Jupyter
jupyter notebook advanced_pipeline_tutorial.ipynb
```

### Quick Run

If you just want to see the results without deep dive:

```python
# Run all cells in order (Shift + Enter)
# Total runtime: ~5-7 minutes
# Generates: performance plots, drift analysis, A/B test results
```

---

## 📊 Scenario

You're a Machine Learning Engineer at an enterprise email security company managing a phishing detection system.

**Timeline:**
- **January 2024**: Train and deploy model v1.0
- **February-July 2024**: Stable production operation
- **August 2024**: Drift detected (attackers adapt tactics)
- **September 2024**: Retrain model v2.0, A/B testing
- **October 2024**: Deploy v2.0, continue monitoring

**Challenges:**
- 📈 False positive rates increasing (alert fatigue)
- 📉 Detection rates decreasing (missed attacks)
- 🔄 Attackers evolving (more sophisticated campaigns)

**Your Mission:**  
Implement a continuous improvement system to maintain model effectiveness over time.

---

## 🔑 Key Concepts Covered

### 1. Production Deployment (Steps 5-6)
- Model serving infrastructure
- Real-time scoring functions
- Prediction logging
- Inference latency monitoring

### 2. Performance Monitoring (Step 7)
- Daily TPR/FPR/Precision tracking
- 7-day and 30-day rolling averages
- Alert threshold configuration
- Monitoring dashboards

### 3. Concept Drift Detection (Steps 8-10)
- **Sudden Drift**: New malware family released
- **Gradual Drift**: APT TTP refinement
- **Statistical Tests**: Kolmogorov-Smirnov test
- **Performance Triggers**: TPR drops >5%, FPR increases >50%

### 4. Analyst Feedback (Step 11)
- True positive/false positive corrections
- Confidence-weighted labeling
- Active learning sample selection
- Feedback aggregation

### 5. Automated Retraining (Steps 12-13)
- **Triggered Retraining**: Performance/drift thresholds
- **Periodic Retraining**: Scheduled intervals
- **Data Collection**: Historical + recent labeled data
- **Validation**: Temporal split (train on past, test on future)

### 6. A/B Testing (Steps 14-15)
- Parallel deployment (v1.0 vs v2.0)
- Traffic splitting (50/50)
- Statistical comparison (McNemar's test)
- Significance testing (p-value < 0.05)

### 7. Gradual Rollout (Step 16)
- **Phase 1**: 10% traffic to v2.0 (monitor 2 days)
- **Phase 2**: 50% traffic to v2.0 (monitor 3 days)
- **Phase 3**: 100% traffic to v2.0 (full deployment)
- **Rollback**: If FPR increases >50%

### 8. Continuous Improvement (Step 17)
- Full cycle visualization
- Performance timeline
- Model version history
- Feedback loop diagram

---

## 📈 Expected Results

With default parameters, you should see:

**Model v1.0 (Jan-Jul 2024):**
- TPR: 85-90%
- FPR: 3-5%
- Precision: 70-80%
- ROC-AUC: 0.90-0.95

**Drift Period (Aug 2024):**
- TPR drops to: 70-75% (⚠️ degradation)
- FPR increases to: 6-8%
- Precision drops to: 60-70%
- Drift detected: KS test p-value < 0.05

**Model v2.0 (Sep-Oct 2024):**
- TPR improves to: 88-93%
- FPR reduces to: 2-4%
- Precision improves to: 75-85%
- Statistical improvement: McNemar p-value < 0.01

**A/B Test Results:**
- v2.0 significantly better than v1.0
- Recommendation: Deploy v2.0
- Expected alert reduction: 20-30%

---

## 🔗 Related Resources

### Prerequisites
- **Exercise 5.2A**: Simple ML Pipeline Tutorial (MUST complete first!)
- **Chapter 5, Section 5.2**: Model Construction
- **Chapter 6, Section 6.1**: Final Model Validation

### Follow-Up
- **Exercise 5.4A**: ROC & Youden Index (`../youden_demo/02_roc_youden_threshold.ipynb`)
- **Chapter 6, Section 6.3**: Long-Term Maintenance & Operations
- **ML_PIPELINE_FLOW.md**: Complete pipeline documentation

### References
- Kolmogorov-Smirnov Test: [scipy.stats.ks_2samp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.ks_2samp.html)
- McNemar's Test: Statistical comparison of classifiers
- A/B Testing: [Experimentation Platform Best Practices](https://exp-platform.com/)

---

## 💡 Practice Challenges

After completing the main tutorial, try these extensions:

### Challenge 1: Ensemble Approach (Advanced)
Combine v1.0 and v2.0 predictions using weighted voting. Does the ensemble outperform individual models?

**Hints:**
- Try weights: 0.3 × v1.0 + 0.7 × v2.0
- Optimize weights on validation set
- Compare ensemble ROC-AUC vs individual models

### Challenge 2: Active Learning (Advanced)
Identify most uncertain predictions (probability ~0.5) for analyst labeling. Measure efficiency gain.

**Hints:**
- Sort by `|probability - 0.5|` (uncertainty)
- Label top 100 uncertain samples
- Retrain and compare to random sampling

### Challenge 3: Cost-Weighted Retraining (Expert)
If FP costs $5 and FN costs $10,000:
- Adjust SMOTE sampling ratio
- Use class weights in Random Forest
- Optimize threshold for minimum total cost

**Hints:**
- Calculate expected cost: `cost = 5*FP + 10000*FN`
- Grid search over thresholds
- Plot cost vs threshold curve

### Challenge 4: Multi-Wave Drift (Expert)
Simulate 3 drift waves (Aug, Nov, Feb). Does v2.0 also degrade? When to retrain again?

**Hints:**
- Generate drift data for 3 periods
- Track v2.0 performance over time
- Implement periodic retraining (quarterly)

### Challenge 5: Feature Importance Drift (Research)
Track top 3 features over time. Do importance rankings shift during drift?

**Hints:**
- Extract `model.feature_importances_` for v1.0 and v2.0
- Compare rankings
- Implications for interpretability and analyst trust

---

## 📝 Assessment

Optional grading rubric (100 points):

| Component | Points | Criteria |
|-----------|--------|----------|
| **Notebook Completion** | 20 | All 17 steps executed successfully |
| **Drift Detection** | 20 | Correctly identify drift in August, explain KS test results |
| **Retraining Pipeline** | 20 | Model v2.0 trained and validated properly |
| **A/B Testing** | 20 | Statistical comparison performed, deployment decision justified |
| **Challenges** | 10 | At least 1 challenge completed |
| **Documentation** | 10 | Clear explanations, visualizations labeled, insights documented |

**Passing Grade**: 70/100

---

## 🐛 Troubleshooting

### Import Error: `ModuleNotFoundError: No module named 'scipy'`
```powershell
pip install scipy>=1.10.0
```

### Import Error: `ModuleNotFoundError: No module named 'tqdm'`
```powershell
pip install tqdm>=4.64.0
```

### Performance Warning: "KS test slow on large data"
Reduce sample size in Step 9:
```python
# Sample 1000 points instead of full dataset
sample_size = 1000
```

### Memory Error: "MemoryError during SMOTE"
Reduce training data size in Step 2:
```python
train_data = generate_email_dataset(n_samples=500, ...)  # Instead of 1000
```

### Plots not showing
Add to first code cell:
```python
%matplotlib inline
```

---

## 📧 Support

- Review **IMPLEMENTATION_PLAN.md** for detailed technical specs
- Check main Exercises README: `../README.md`
- Consult **ML_PIPELINE_FLOW.md** for conceptual background
- Contact course instructor or TA for assistance

---

## 📊 File Structure

```
5.2A_Advanced_Pipeline/
├── README.md                              # This file
├── IMPLEMENTATION_PLAN.md                 # Technical specification
├── advanced_pipeline_tutorial.ipynb       # Main tutorial notebook
├── requirements_advanced_tutorial.txt     # Python dependencies
├── generate_notebook.py                   # Notebook generation script
├── model_v1.0.pkl                         # Generated: Baseline model
├── model_v2.0.pkl                         # Generated: Retrained model
├── scaler_v1.0.pkl                        # Generated: Feature scaler
└── production_logs.csv                    # Generated: Time series data
```

---

**Version:** 1.0  
**Created:** November 26, 2025  
**Exercise:** 5.2A.1 (Advanced Production ML Pipeline)  
**Module:** 3, Chapter 5 - ML Algorithm Development Pipeline  
**Estimated Time:** 90-120 minutes  
**Difficulty:** Advanced  
**Prerequisites:** Exercise 5.2A (Simple Pipeline)
