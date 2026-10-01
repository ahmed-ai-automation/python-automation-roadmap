"""
Module: helpers/text_utils.py
Description: Text processing helper functions for modular imports.
Unit: 06 - Modules & Packages
"""

def clean_text(text):
    """Strips whitespace and converts text to lowercase."""
    if not text:
        return ""
    return text.strip().lower()


def format_log_message(level, message):
    """Formats a standard log string."""
    clean_msg = clean_text(message)
    return f"[{level.upper()}] {clean_msg}"


if __name__ == "__main__":
    # Test execution context only when running this file directly
    print("Testing text_utils module directly:")
    print(format_log_message("info", "  Testing Text Helper  "))