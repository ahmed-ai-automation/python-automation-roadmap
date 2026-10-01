"""
Module: 06_modular_automation.py
Description: Demonstrates standard library modules (json, datetime, os) and custom module imports.
Unit: 06 - Modules & Packages
"""

import json
import os
from datetime import datetime

# Importing from custom helper package
from helpers.text_utils import clean_text, format_log_message


def process_automation_payload(raw_json_data):
    """Processes incoming JSON text using standard libraries and custom modules."""
    try:
        # Parsing JSON string using standard library
        data = json.loads(raw_json_data)
        
        # Accessing nested structures
        status = clean_text(data.get("status", ""))
        payload_id = data.get("id", "UNKNOWN")
        
        # Getting current execution timestamp using datetime module
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = format_log_message("INFO", f"Processed ID: {payload_id} | Status: {status} | Time: {timestamp}")
        return True, log_entry

    except json.JSONDecodeError as e:
        error_log = format_log_message("ERROR", f"Failed to parse JSON payload: {e}")
        return False, error_log


def main():
    """Main execution function."""
    print("=" * 60)
    print("MODULAR AUTOMATION WORKFLOW DEMO")
    print("=" * 60)
    
    # Simulating raw JSON API payload
    raw_payload = '{"id": "JOB-8841", "status": " PENDING_EXECUTION "}'
    
    # Processing payload
    success, log_message = process_automation_payload(raw_payload)
    print(log_message)
    
    # Standard library OS information
    current_directory = os.getcwd()
    print(format_log_message("SYSTEM", f"Current working directory: {current_directory}"))
    print("=" * 60)


if __name__ == "__main__":
    # Ensures main() executes only when run directly, not when imported
    main()