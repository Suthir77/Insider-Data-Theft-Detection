Tool Name: Insider Threat Detector

Purpose: This tool uses a simple rule-based AI-inspired approach to detect possible insider data theft activity based on sample forensic indicators.

Input: sample_activity_log.csv

How to Run: python insider_threat_detector.py

Rules Used:

1. Sensitive data indicators such as employee-related records, confidential files, and business documents.
2. Possible exfiltration indicators such as USB activity, removable device usage, external email, and web activity.
3. Suspicious behaviour indicators such as recent document access and multiple timeline events.

Output: The tool calculates a risk score and classifies the activity as LOW, MEDIUM, or HIGH risk.

Note: This repository does not include the original forensic image, Autopsy case files, or sensitive evidence exports. The CSV file is sample/demo data only.

Conclusion: The tool supports forensic investigation by highlighting suspicious behaviour patterns from sample activity indicators.
