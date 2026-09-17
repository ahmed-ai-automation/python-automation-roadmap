# Unit 05: Error Handling & Resilience for Automation

## Overview
This unit focuses on managing runtime execution exceptions, implementing fallback strategies, and mastering resource cleanup using `try`, `except`, `else`, and `finally` with built-in exceptions.

## Key Concepts Implemented
- **Built-in Exceptions:** Utilizing native Python exceptions (`ValueError`, `ConnectionError`, `TypeError`) via `raise`.
- **Exception Isolation:** Differentiating between expected issues (network/validation) and unexpected bugs using specific `except` blocks.
- **Resource Cleanup (`else` & `finally`):**
  - `else`: Executing post-success operations safely when no exceptions occur.
  - `finally`: Ensuring connection buffers and resource cleanups execute regardless of failure.
- **Strategy:** Graceful degradation on expected API failures without suppressing critical system bugs.

## How to Run
```bash
python 05-error-handling/05_resilient_api_handling.pys