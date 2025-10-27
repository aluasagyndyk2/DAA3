# utils.py
# Utility functions: read input JSON and write output JSON.
import json
from typing import Any, Dict

def read_input(path: str) -> Dict[str, Any]:
    """Read input JSON file and return parsed data."""
    with open(path, 'r') as f:
        return json.load(f)

def write_output(path: str, data: Dict[str, Any]) -> None:
    """Write the output data to a JSON file with pretty formatting."""
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)
