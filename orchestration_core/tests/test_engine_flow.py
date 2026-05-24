# orchestration_core/tests/test_engine_flow.py

from orchestration_core.api.entry import receive_input

def test_emergency_flow():
    response = receive_input("emergency chest pain", "t1")

    assert response["status"] == "OK"
    assert response["session"]["emergency"] is True
    assert response["session"]["emergency_details"]["is_emergency"] is True