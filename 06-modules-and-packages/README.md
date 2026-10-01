# Unit 06: Modules, Packages & Project Structure

## Overview
This unit introduces code modularity, package structuring, import mechanisms, standard library usage (`json`, `datetime`, `os`), and execution context management (`if __name__ == "__main__"`).

## Key Concepts Implemented
- **Custom Modules & Packages:** Creating reusable modules (`text_utils.py`) inside a package directory with `__init__.py`.
- **Import Strategies:** Using explicit function imports (`from helpers.text_utils import clean_text`).
- **Standard Library Modules:**
  - `json`: Parsing and processing structured string data.
  - `datetime`: Generating execution timestamps.
  - `os`: Interacting with operating system paths and working directories.
- **Execution Context:** Utilizing `if __name__ == "__main__":` to separate executable code from importable module logic.

## How to Run
```bash
python 06-modules-and-packages/06_modular_automation.py