from datetime import datetime
import json
import os

AUDIT_LOG_PATH = "runtime/logs/audit.log"


def write_audit_log(
    request_id: str,
    timestamp: str,
    input_text: str,
    response: dict
):
    entry = {
        "request_id": request_id,
        "timestamp": timestamp,
        "input_text": input_text,
        "response": response
    }

    os.makedirs(os.path.dirname(AUDIT_LOG_PATH), exist_ok=True)

    with open(AUDIT_LOG_PATH, "a") as f:
        f.write(json.dumps(entry) + "\n")