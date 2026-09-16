"""
Module: 01_data_cleaning_pipeline.py
Description: Fundamentals project simulating text & prompt data preparation for AI pipelines.
Unit: 01 - Python Fundamentals
"""

# --- 1. Variables, Constants & Dynamic Typing ---
DEFAULT_STATUS = "PENDING"
API_VERSION = "v1.0"

# Uncleaned payload sample coming from an external source (e.g., API or Email)
raw_user_input = "   AHMED_HASSAN@EXAMPLE.COM   "
raw_lead_score = " 95 "
raw_notes = None

# --- 2. String Manipulation & Data Cleaning ---
# Strip whitespace and convert to lowercase
clean_email = raw_user_input.strip().lower()

# Extract domain using string slicing and find()
at_index = clean_email.find("@")
email_domain = clean_email[at_index + 1 :]

# Verify email structure using string methods
is_valid_email = clean_email.endswith(".com") and ("@" in clean_email)

# --- 3. Type Conversion & Truthiness Handling ---
# Safely convert lead score from string to integer
lead_score = int(raw_lead_score.strip())

# Truthiness check for notes (Handling None vs Empty String)
has_notes = bool(raw_notes)
processed_notes = raw_notes if has_notes else "No notes provided"

# --- 4. Operators & Logical Verification ---
# Identity vs Equality checks
is_same_status = DEFAULT_STATUS == "PENDING"
is_none_check = raw_notes is None

# High-priority lead threshold verification
is_high_value = (lead_score >= 80) and is_valid_email

# --- 5. Output Formatting for Automation Logs (f-strings) ---
log_separator = "=" * 50

print(log_separator)
print(f"SYSTEM LOG [{API_VERSION}] - DATA CLEANING COMPLETE")
print(log_separator)
print(f"Cleaned Email : {clean_email}")
print(f"Domain Extracted: {email_domain}")
print(f"Is Valid Email : {is_valid_email}")
print(f"Lead Score     : {lead_score} (Type: {type(lead_score).__name__})")
print(f"High Value Lead: {is_high_value}")
print(f"Notes Status   : {processed_notes}")
print(log_separator)