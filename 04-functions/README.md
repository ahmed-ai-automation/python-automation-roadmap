# Unit 04: Functions & Function Design for Automation

## Overview
This unit covers pure function principles, dynamic argument mechanics (`*args` and `**kwargs`), argument unpacking, functional concepts like Lambdas, passing functions as objects, and scope isolation rules.

## Key Concepts Implemented
- **Pure Functions & Default Arguments:** Defining reusable blocks with default parameters (`cost_per_token=0.00002`).
- **Flexible Arguments & Unpacking:**
  - `*args`: Gathering variable positional text messages dynamically.
  - `**kwargs`: Capturing dynamic configuration parameters.
  - Dictionary Unpacking: Unpacking dictionaries directly into functions (`**runtime_config`).
- **Functional Programming Concepts:**
  - **Functions as First-Class Objects:** Passing function references as arguments into pipeline functions (`process_text_pipeline`).
  - **Lambda Functions:** Utilizing anonymous inline functions for quick string transformations and `sorted()` keys.
- **Scope Isolation:** Writing modular functions without relying on `global` mutable state.

## How to Run
```bash
python 04-functions/04_function_architecture.py