from orchestration_core.audit.ledger import (
    init_ledger,
    verify_ledger_integrity
)
from orchestration_core.api.entry import receive_input


def test_audit_hash_chain():
    init_ledger()
    receive_input("emergency chest pain", "audit1")
    receive_input("normal query", "audit2")

    assert verify_ledger_integrity() is True