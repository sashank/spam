# Exercise 5.2A_Spam - Email Components Primer

This short, self-contained exercise is a precursor to Exercises 5.2A (Simple Pipeline) and 5.2A.1 (Advanced Pipeline).

Goal: Introduce students to the anatomy of email-based threats (spam, phishing, BEC), show sample raw emails, and walk through which fields and content to extract for ML pipelines.

Quick Start:

```powershell
cd content/modules/Module_03_Data_Science_ML_Foundations/Chapter5/Exercises/5.2A_Spam
pip install -r requirements.txt  # optional, standard library used
jupyter notebook 5.2A_Spam.ipynb
```

What's included:
- `5.2A_Spam.ipynb` - Notebook with examples and parsing code
- `requirements.txt` - Minimal dependency file (empty/standard library)

Learning outcomes:
- Identify header fields useful for detection (From, To, Received, SPF/DKIM headers)
- Recognize body cues (links, call to action, urgency, misspellings)
- Understand attachments and their metadata (filename, MIME type, size)
- Know which features to extract for downstream ML pipelines

Instructor notes:
- Notebook is designed to run offline with synthetic samples
- Encourage students to experiment by modifying sample emails to see feature changes
