import csv

def calculate_risk_score(log_file):
    risk_score = 0
    findings = []

    sensitive_keywords = ["salary", "ssn", "sensitive", "employee", "m57biz"]
    exfiltration_keywords = ["usb", "flash drive", "removable", "gmail", "yahoo", "web"]
    suspicious_keywords = ["timeline", "recent document", "accessed", "short time"]

    with open(log_file, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            description = row["description"].lower()
            event_type = row["event_type"]

            if any(keyword in description for keyword in sensitive_keywords):
                risk_score += 30
                findings.append(f"[Sensitive Data] {row['description']}")

            if any(keyword in description for keyword in exfiltration_keywords):
                risk_score += 25
                findings.append(f"[Possible Exfiltration] {row['description']}")

            if any(keyword in description for keyword in suspicious_keywords):
                risk_score += 20
                findings.append(f"[Suspicious Behaviour] {row['description']}")

    if risk_score >= 80:
        risk_level = "HIGH"
    elif risk_score >= 50:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    print("Insider Threat Detection Result")
    print("--------------------------------")
    print(f"Risk Score: {risk_score}")
    print(f"Risk Level: {risk_level}")
    print("\nFindings:")

    for finding in findings:
        print(f"- {finding}")

    print("\nConclusion:")
    if risk_level == "HIGH":
        print("The evidence indicates a high possibility of insider data theft activity.")
    elif risk_level == "MEDIUM":
        print("The evidence indicates suspicious activity that requires further investigation.")
    else:
        print("The evidence does not strongly indicate insider data theft.")

if __name__ == "__main__":
    calculate_risk_score("activity_log.csv")