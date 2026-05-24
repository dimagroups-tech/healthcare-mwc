# tests/test_engine_flow.py

import pytest

from api.entry import receive_input
from reasoning.audit_logger import get_audit_log, clear_audit_log
from reasoning.session_store import get_session


@pytest.fixture(autouse=True)
def reset_state():
    """
    Runs before every test.
    Clears audit log and resets in-memory sessions.
    """
    clear_audit_log()


def test_emergency_flow_triggers_policy_and_audit():
    result = receive_input("emergency chest pain", "t1")

    # Response validation
    assert result["status"] == "OK"
    assert result["session"]["emergency"] is True
    assert "emergency" in result["message"].lower()

    # Session validation
    session = get_session("t1")
    assert session["emergency"] is True
    assert "emergency_details" in session

    # Audit validation
    events = get_audit_log()
    event_types = [e["event_type"] for e in events]

    assert "INPUT_RECEIVED" in event_types
    assert "EMERGENCY_TRIGGERED" in event_types


def test_city_then_hospital_flow():
    r1 = receive_input("Manipal", "t2")
    assert r1["session"]["city"] == "Manipal"
    assert r1["session"]["hospital"] is None

    r2 = receive_input("KMC Hospital", "t2")
    assert r2["session"]["city"] == "Manipal"
    assert r2["session"]["hospital"] == "KMC Hospital"

    events = get_audit_log()
    messages = [e["event_type"] for e in events]

    assert "CITY_SET" in messages
    assert "HOSPITAL_SET" in messages


def test_no_state_change_input():
    receive_input("Manipal", "t3")
    receive_input("KMC Hospital", "t3")
    receive_input("hello", "t3")

    events = get_audit_log()
    last_event = events[-1]

    assert last_event["event_type"] == "NO_STATE_CHANGE"


def test_sessions_are_isolated():
    receive_input("Manipal", "s1")
    receive_input("emergency chest pain", "s2")

    s1 = get_session("s1")
    s2 = get_session("s2")

    assert s1["emergency"] is False
    assert s2["emergency"] is True
    assert s1["city"] == "Manipal"
    assert s2["city"] is None