"""
Module: 05_resilient_api_handling.py
Description: Robust error handling strategy using try/except/else/finally without custom classes.
Unit: 05 - Error Handling
"""

def mock_external_api_call(payload):
    """
    Simulates an external API call that raises built-in exceptions 
    based on payload validity and connectivity status.
    """
    if payload is None:
        # Simulate connection or value errors using built-in exceptions
        raise ConnectionError("Failed to connect to API endpoint: Timeout")
    
    if "email" not in payload or not payload["email"]:
        # Simulate invalid input payload error
        raise ValueError("Missing required field: 'email'")
        
    if payload.get("trigger_type_error"):
        # Simulate unexpected type error during execution
        return payload["amount"] + "USD"
        
    return {"status": "success", "status_code": 200, "response_id": "RES-9981"}


def validate_and_process(payload):
    """
    Processes input payload and handles expected vs unexpected errors gracefully.
    """
    email = payload.get("email", "Unknown") if payload else "None"
    print(f"\n--- Processing Payload for: {email} ---")
    
    try:
        # Attempting external execution
        result = mock_external_api_call(payload)
        
    except ConnectionError as e:
        # Handling network connection issues
        print(f"[EXPECTED ERROR] Network Failure: {e}")
        print("Strategy: Triggering Retry Mechanism...")
        return {"status": "failed", "reason": "connection_timeout"}

    except ValueError as e:
        # Handling data validation issues
        print(f"[EXPECTED ERROR] Validation Failure: {e}")
        print("Strategy: Logging bad data and skipping...")
        return {"status": "failed", "reason": "invalid_data"}

    except Exception as e:
        # Handling unexpected critical failures
        print(f"[UNEXPECTED ERROR] {type(e).__name__}: {e}")
        print("Strategy: Don't hide errors! Reporting critical bug...")
        return {"status": "critical_failure", "error_type": type(e).__name__}

    else:
        # Executes only when try block succeeds without exceptions
        print(f"[SUCCESS] Execution successful. Status Code: {result['status_code']}")
        return result

    finally:
        # Always executes for cleanup operations
        print("[CLEANUP] Closing API connection session...")


# --- Execution Tests ---

# Test Case 1: Valid Payload (Success Path)
valid_payload = {"email": "ahmed@example.com", "trigger_type_error": False}
res1 = validate_and_process(valid_payload)

# Test Case 2: Invalid Payload (ValueError)
invalid_payload = {"email": "", "trigger_type_error": False}
res2 = validate_and_process(invalid_payload)

# Test Case 3: Connection Timeout (ConnectionError)
timeout_payload = None
res3 = validate_and_process(timeout_payload)

# Test Case 4: Unexpected Error (TypeError)
unexpected_payload = {"email": "test@example.com", "amount": 100, "trigger_type_error": True}
res4 = validate_and_process(unexpected_payload)

print("\n" + "=" * 60)
print("EXECUTION SUMMARY LOG")
print("=" * 60)
print(f"Valid Payload Result     : {res1['status']}")
print(f"Invalid Payload Result   : {res2['status']}")
print(f"Timeout Payload Result   : {res3['status']}")
print(f"Unexpected Error Result  : {res4['status']}")
print("=" * 60)