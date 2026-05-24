import hashlib
import json

LEDGER = []


def init_ledger():
    LEDGER.clear()


def _hash_entry(entry: dict, prev_hash: str) -> str:
    payload = json.dumps(entry, sort_keys=True) + prev_hash
    return hashlib.sha256(payload.encode()).hexdigest()


def append_audit_event(session_id: str, step: str, data: dict):
    prev_hash = LEDGER[-1]["hash"] if LEDGER else "GENESIS"

    entry = {
        "session_id": session_id,
        "step": step,
        "data": data,
        "prev_hash": prev_hash,
    }

    entry["hash"] = _hash_entry(entry, prev_hash)
    LEDGER.append(entry)


def verify_ledger_integrity() -> bool:
    prev_hash = "GENESIS"

    for entry in LEDGER:
        expected = _hash_entry(
            {
                "session_id": entry["session_id"],
                "step": entry["step"],
                "data": entry["data"],
                "prev_hash": entry["prev_hash"],
            },
            prev_hash,
        )

        if entry["hash"] != expected:
            return False

        prev_hash = entry["hash"]

    return True