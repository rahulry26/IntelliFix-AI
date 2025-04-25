# parse_alert.py

import json

def parse_alert(file_path):
    with open(file_path) as f:
        alert = json.load(f)
    
    combined_text = f"""
    Alert: {alert['alertname']}
    Severity: {alert['severity']}
    Instance: {alert['instance']}
    Description: {alert['description']}
    Logs: {" ".join(alert['logs'])}
    Timestamp: {alert['timestamp']}
    """
    return combined_text.strip()


