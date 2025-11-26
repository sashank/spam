# Exercise 5.2A.1: Advanced Pipeline Implementation Plan

## 🎯 Goal
Create a comprehensive advanced ML pipeline tutorial demonstrating the complete **Continuous Improvement Cycle** from Chapter 6.3 of ML_PIPELINE_FLOW.md, extending the phishing detection example from Exercise 5.2A.

---

## 📋 Complete Step-by-Step Structure

### **Phase 1: Initial Setup & Baseline (Steps 1-4)**
Reuse and extend 5.2A simple pipeline foundation

**Step 1: Import Libraries**
- Core ML libraries (sklearn, pandas, numpy)
- **NEW**: scipy.stats (KS test for drift)
- **NEW**: datetime (temporal simulation)
- **NEW**: tqdm (progress tracking)
- **NEW**: warnings (clean output)

**Step 2: Generate Initial Training Data**
- Same phishing dataset from 5.2A
- 1,000 samples (90% legit, 10% phishing)
- Timestamp: January 2024

**Step 3: Train Baseline Model (v1.0)**
- Random Forest with SMOTE
- Feature scaling
- Initial metrics: ROC-AUC, Precision, Recall
- **Save as**: `model_v1.0.pkl`

**Step 4: Create Model Version Tracker**
- Dictionary storing: version, timestamp, metrics, model object
- Performance log DataFrame

---

### **Phase 2: Production Deployment & Monitoring (Steps 5-7)**

**Step 5: Deploy Model v1.0 to Production**
- Simulate production scoring function
- Log predictions with probabilities
- Track inference time

**Step 6: Simulate Time-Series Production Traffic**
- Generate 6 months of daily email batches (Feb-Jul 2024)
- Maintain ~10% phishing rate initially
- Apply model v1.0 to all batches
- Store: date, predictions, actuals, probabilities

**Step 7: Production Monitoring Dashboard**
- Track **daily** metrics: TPR, FPR, Precision, F1
- **7-day rolling average** (smooth noise)
- **30-day rolling average** (long-term trend)
- Visualization: 3-panel plot
  - Panel 1: TPR over time (target: >90%)
  - Panel 2: FPR over time (target: <5%)
  - Panel 3: Precision over time (target: >75%)
- Alert thresholds marked on plots

---

### **Phase 3: Concept Drift Simulation (Steps 8-10)**

**Step 8: Simulate Attacker Adaptation (August 2024)**
- **NEW phishing tactics**:
  - Reduced urgency_words (evade detection)
  - Better sender_reputation mimicry
  - More sophisticated email_length distribution
- Generate "drifted" phishing samples
- Performance degradation expected

**Step 9: Detect Concept Drift Automatically**
- **Kolmogorov-Smirnov (KS) Test**:
  - Compare feature distributions: July vs August
  - Test each feature individually
  - Aggregate drift score
- **Performance-based detection**:
  - TPR drops >5% from baseline
  - FPR increases >50% from baseline
  - Precision drops >10%
- Trigger: If drift score > threshold OR performance degraded

**Step 10: Visualize Drift Analysis**
- Feature distribution comparison (before/after)
- KS test p-values bar chart
- Performance degradation timeline

---

### **Phase 4: Feedback Collection & Retraining (Steps 11-13)**

**Step 11: Analyst Feedback Loop**
- Simulate SOC analyst review:
  - Review top 100 alerts from August
  - Correct labels (mark FP/FN)
  - Prioritize high-confidence errors
- Store feedback: sample_id, original_label, corrected_label, analyst_confidence

**Step 12: Automated Retraining Pipeline**
- **Data Collection**:
  - Original training data (Jan-July)
  - New labeled data (August with analyst corrections)
  - SMOTE on combined dataset
- **Feature Engineering**:
  - Same pipeline as v1.0 (consistency)
  - Optional: Add new features based on drift analysis
- **Model Training**:
  - Random Forest with optimized hyperparameters
  - Train on expanded dataset
  - **Save as**: `model_v2.0.pkl`
- **Validation**:
  - Temporal validation: Test on September data
  - Calculate metrics on validation set

**Step 13: Model v2.0 Performance Report**
- Compare v1.0 vs v2.0 on **same test set** (September)
- Metrics table with improvement percentages
- Confusion matrix comparison

---

### **Phase 5: A/B Testing & Deployment (Steps 14-16)**

**Step 14: A/B Test Framework**
- Simulate **September production traffic**
- Split traffic 50/50:
  - Group A: Model v1.0 (control)
  - Group B: Model v2.0 (treatment)
- Track metrics independently
- Statistical power: 1,000+ samples per group

**Step 15: Statistical Significance Testing**
- **McNemar's Test**:
  - Compare predictions on same samples
  - Null hypothesis: Models perform equally
  - p-value < 0.05 → significant improvement
- **Paired metrics comparison**:
  - TPR: v1.0 vs v2.0
  - FPR: v1.0 vs v2.0
  - Precision: v1.0 vs v2.0

**Step 16: Gradual Rollout (Canary Deployment)**
- **Phase 1**: 10% traffic to v2.0, 90% to v1.0 (monitor 2 days)
- **Phase 2**: 50% traffic to v2.0, 50% to v1.0 (monitor 3 days)
- **Phase 3**: 100% traffic to v2.0 (full deployment)
- Rollback capability: If v2.0 FPR > v1.0 by 50%
- Visualize: Traffic allocation over time

---

### **Phase 6: Complete Continuous Improvement Loop (Step 17)**

**Step 17: Full Cycle Visualization & Summary**
- **Timeline visualization**:
  - Jan-Jul: v1.0 training & deployment
  - Aug: Drift detection
  - Sep: Retraining & A/B testing
  - Oct: v2.0 full deployment
- **Key metrics dashboard**:
  - Model version history
  - Performance trends
  - Drift events marked
  - Retraining triggers
- **Feedback loop diagram**:
  ```
  Production → Monitor → Detect Drift → Collect Feedback
       ↑                                      ↓
  Deploy ← Validate ← Retrain ← Re-engineer Features
  ```

---

## 🎓 Practice Challenges (Extensions)

### Challenge 1: Ensemble Approach
Combine v1.0 and v2.0 predictions (weighted voting). Does ensemble outperform individual models?

### Challenge 2: Active Learning
Identify most uncertain predictions (probability ~0.5). Simulate analyst labeling only those. Retrain and measure efficiency gain.

### Challenge 3: Cost-Weighted Retraining
If FP costs $5 and FN costs $10,000:
- Adjust SMOTE sampling ratio
- Use class weights in Random Forest
- Optimize threshold for minimum total cost

### Challenge 4: Multi-Wave Drift
Simulate 3 drift waves (Aug, Nov, Feb). Does v2.0 also degrade? When to retrain again?

### Challenge 5: Feature Importance Drift
Track top 3 features over time. Do importance rankings shift during drift? Implications for interpretability?

---

## 📊 Expected Learning Outcomes

✅ **Understand Production ML Lifecycle**
- Initial deployment is just the beginning
- Models degrade over time (concept drift)
- Continuous monitoring is critical

✅ **Master Drift Detection**
- Statistical tests (KS test)
- Performance-based monitoring
- Feature distribution changes

✅ **Implement Feedback Loops**
- Analyst corrections improve models
- Active learning reduces labeling cost
- Closed-loop system design

✅ **Practice Model Comparison**
- Statistical significance (McNemar's test)
- A/B testing in production
- Risk mitigation (canary deployments)

✅ **Operationalize ML Security Systems**
- Version control for models
- Rollback strategies
- Gradual rollout procedures

---

## 🔧 Technical Requirements

### Python Packages
```
# Core ML (from 5.2A)
pandas>=1.5.0
numpy>=1.23.0
scikit-learn>=1.2.0
imbalanced-learn>=0.10.0
matplotlib>=3.6.0
seaborn>=0.12.0
joblib>=1.2.0

# NEW for Advanced Pipeline
scipy>=1.10.0          # KS test, statistical tests
tqdm>=4.64.0           # Progress bars for time series
datetime               # Built-in (temporal simulation)
```

### Data Volumes
- Initial training: 1,000 samples
- Production simulation: ~180 days × 100 emails/day = 18,000 samples
- Total dataset: ~20,000 samples (manageable in memory)

### Computation Time
- Initial training: ~10 seconds
- Time series simulation: ~60 seconds (180 iterations)
- Retraining: ~15 seconds
- A/B testing: ~30 seconds
- **Total runtime**: ~5-7 minutes (acceptable for tutorial)

---

## 📁 File Structure

```
5.2A_Advanced_Pipeline/
├── README.md                              # Overview, quick start
├── IMPLEMENTATION_PLAN.md                 # This file (detailed spec)
├── advanced_pipeline_tutorial.ipynb       # Main tutorial (17 steps)
├── ADVANCED_PIPELINE_TUTORIAL.md          # Teaching assistant guide
├── requirements_advanced_tutorial.txt     # Python dependencies
├── model_v1.0.pkl                         # Generated: Initial model
├── model_v2.0.pkl                         # Generated: Retrained model
├── scaler_v1.0.pkl                        # Generated: Feature scaler
├── production_logs.csv                    # Generated: Time series data
└── performance_history.csv                # Generated: Monitoring data
```

---

## 🚀 Implementation Sequence

1. ✅ **Phase 1**: Create notebook structure, Steps 1-4 (baseline)
2. ⏳ **Phase 2**: Add Steps 5-7 (monitoring)
3. ⏳ **Phase 3**: Add Steps 8-10 (drift detection)
4. ⏳ **Phase 4**: Add Steps 11-13 (retraining)
5. ⏳ **Phase 5**: Add Steps 14-16 (A/B testing)
6. ⏳ **Phase 6**: Add Step 17 (full loop)
7. ⏳ **Documentation**: README, teaching guide, requirements
8. ⏳ **Integration**: Update main Exercises README

---

## 📖 Relationship to ML_PIPELINE_FLOW.md

| ML_PIPELINE_FLOW Section | Advanced Pipeline Step | Implementation |
|--------------------------|------------------------|----------------|
| **6.2 Deployment** | Steps 5-6 | Production scoring function |
| **6.3.1 Concept Drift** | Steps 8-10 | Attacker adaptation simulation |
| **6.3 Monitoring** | Step 7 | TPR/FPR/Precision dashboards |
| **6.3 Drift Detection** | Step 9 | KS test, performance thresholds |
| **6.3 Feedback Loops** | Step 11 | Analyst corrections |
| **6.3.2 Retraining** | Step 12 | Automated pipeline |
| **6.3 A/B Testing** | Steps 14-15 | Statistical comparison |
| **6.3 Gradual Rollout** | Step 16 | Canary deployment |
| **6.3 Continuous Improvement** | Step 17 | Full cycle visualization |

---

**Status**: Planning Complete ✅  
**Next**: Begin Phase 1 implementation  
**Estimated Total LOC**: ~1,500 lines (notebook + documentation)  
**Estimated Dev Time**: 4-6 hours (systematic implementation)
