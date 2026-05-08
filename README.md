Tool Name:
Insider Threat Detector

Purpose:
This tool uses a simple rule-based AI-inspired approach to detect possible insider data theft activity based on forensic evidence collected from Autopsy.

Input:
activity_log.csv

How to Run:
python insider_threat_detector.py

Rules Used:
1. Sensitive data indicators such as employee-related records, confidential files, and business documents.
2. Possible exfiltration indicators such as USB, flash drive, removable device, Gmail, Yahoo, and web activity.
3. Suspicious behaviour indicators such as recent document access and multiple timeline events.

Output:
The tool calculates a risk score and classifies the activity as LOW, MEDIUM, or HIGH risk.

Conclusion:
The tool supports the forensic investigation by highlighting suspicious behaviour patterns from the collected evidence.
