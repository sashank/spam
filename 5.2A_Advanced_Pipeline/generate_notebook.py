"""
Script to generate the complete advanced_pipeline_tutorial.ipynb
Run this to create the full notebook with all 17 steps.
"""

import json

# This will contain all cells for the notebook
cells = []

# Helper function to add cells
def add_markdown(content):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": content.split('\n')
    })

def add_code(content):
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": content.split('\n')
    })

# Title and Overview (already added)
# Steps 1-3 (already added)

# Step 4: Version Tracker
add_markdown("""---

## Step 4: Initialize Model Version Tracker

Create a system to track all model versions, their performance metrics, and deployment history.""")

add_code("""# Initialize model version tracker
model_registry = {
    'v1.0': {
        'model': model_v1,
        'scaler': scaler_v1,
        'trained_date': datetime(2024, 1, 31),
        'deployed_date': datetime(2024, 2, 1),
        'training_data_period': '2024-01',
        'metrics': {
            'accuracy': val_acc,
            'precision': val_precision,
            'recall': tpr_v1,
            'f1': val_f1,
            'roc_auc': val_auc,
            'tpr': tpr_v1,
            'fpr': fpr_v1
        },
        'status': 'deployed'
    }
}

# Performance log for production monitoring
performance_log = []

print("✅ Model Version Tracker Initialized")
print(f"\\n📋 Registry:")
for version, info in model_registry.items():
    print(f"   {version}: {info['status']} on {info['deployed_date'].date()}")
    print(f"      TPR: {info['metrics']['tpr']:.1%} | FPR: {info['metrics']['fpr']:.1%}")""")

# Step 5-7: Production Monitoring
add_markdown("""---

# 🚀 PHASE 2: Production Deployment & Monitoring

## Step 5: Deploy Model v1.0 to Production

Simulate deploying model v1.0 to production environment with real-time scoring capability.""")

add_code("""def score_emails(model, scaler, X, return_proba=False):
    \"\"\"
    Score emails using deployed model.
    
    Parameters:
    - model: Trained classifier
    - scaler: Fitted scaler
    - X: Feature DataFrame
    - return_proba: Return probabilities instead of binary predictions
    
    Returns:
    - predictions or probabilities
    \"\"\"
    X_scaled = scaler.transform(X[feature_cols])
    
    if return_proba:
        return model.predict_proba(X_scaled)[:, 1]
    else:
        return model.predict(X_scaled)

print("✅ Production scoring function ready")
print("\\n🔧 Function: score_emails(model, scaler, X, return_proba=False)")
print("   - Input: Email features DataFrame")
print("   - Output: Predictions (0/1) or probabilities")
print("   - Latency: ~10ms per email (simulated)")""")

add_markdown("""## Step 6: Simulate Production Traffic Over Time

Generate 6 months of email traffic (Feb-Jul 2024) with stable phishing patterns initially.""")

add_code("""# Generate production traffic for February - July 2024 (6 months)
print("🔄 Generating production traffic simulation...")
print("   This may take ~30 seconds...\\n")

production_months = []
month_names = ['February', 'March', 'April', 'May', 'June', 'July']
base_dates = [datetime(2024, m, 1) for m in range(2, 8)]

for month_name, base_date in tqdm(zip(month_names, base_dates), total=6, desc="Generating months"):
    # Generate ~3000 emails per month (100/day)
    month_data = generate_email_dataset(
        n_samples=3000,
        phishing_ratio=0.1,
        base_date=base_date,
        drift_level=0  # No drift yet
    )
    month_data['month'] = month_name
    production_months.append(month_data)

# Combine all months
production_data_stable = pd.concat(production_months, ignore_index=True)
production_data_stable = production_data_stable.sort_values('timestamp').reset_index(drop=True)

print(f"\\n✅ Production data generated: {len(production_data_stable):,} emails")
print(f"   Period: {production_data_stable['timestamp'].min().date()} to {production_data_stable['timestamp'].max().date()}")
print(f"   Phishing rate: {(production_data_stable['label'] == 1).sum() / len(production_data_stable) * 100:.1f}%")

# Score all production emails with model v1.0
print("\\n🔮 Scoring production traffic with model v1.0...")
production_data_stable['prediction'] = score_emails(model_v1, scaler_v1, production_data_stable)
production_data_stable['probability'] = score_emails(model_v1, scaler_v1, production_data_stable, return_proba=True)

# Calculate daily metrics
production_data_stable['date'] = production_data_stable['timestamp'].dt.date
daily_metrics = []

for date in production_data_stable['date'].unique():
    day_data = production_data_stable[production_data_stable['date'] == date]
    y_true = day_data['label']
    y_pred = day_data['prediction']
    
    # Calculate confusion matrix
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    tn, fp, fn, tp = cm.ravel()
    
    # Calculate metrics (handle division by zero)
    tpr = tp / (tp + fn) if (tp + fn) > 0 else 0
    fpr = fp / (fp + tn) if (fp + tn) > 0 else 0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tpr
    
    daily_metrics.append({
        'date': date,
        'total_emails': len(day_data),
        'actual_phishing': (y_true == 1).sum(),
        'predicted_phishing': (y_pred == 1).sum(),
        'tp': tp,
        'fp': fp,
        'tn': tn,
        'fn': fn,
        'tpr': tpr,
        'fpr': fpr,
        'precision': precision,
        'recall': recall
    })

metrics_df = pd.DataFrame(daily_metrics)
metrics_df['model_version'] = 'v1.0'

print(f"✅ Scored {len(production_data_stable):,} emails")
print(f"   True Positives: {metrics_df['tp'].sum()}")
print(f"   False Positives: {metrics_df['fp'].sum()}")
print(f"   False Negatives: {metrics_df['fn'].sum()}")
print(f"\\n📊 Average Performance (Feb-Jul 2024):")
print(f"   TPR: {metrics_df['tpr'].mean():.1%}")
print(f"   FPR: {metrics_df['fpr'].mean():.1%}")
print(f"   Precision: {metrics_df['precision'].mean():.1%}")""")

# Now save to continue in next message due to length limits
notebook_content = {
    "cells": cells,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "nbconvert_exporter": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0"
        }
    },
    "nbformat": 4,
    "nbformat_minor": 4
}

print(f"Generated {len(cells)} cells so far...")
print("Note: This is Part 1 - Steps 1-6. Continue building remaining steps...")
