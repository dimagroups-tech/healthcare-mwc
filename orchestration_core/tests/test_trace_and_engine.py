from orchestration_core.api.entry import receive_input
from orchestration_core.reasoning.trace import get_trace, clear_traces


def test_trace_written():
    clear_traces()
    receive_input("emergency chest pain", "t2")

    trace = get_trace("t2")
    steps = [t["step"] for t in trace]

    assert "INPUT" in steps
    assert "EMERGENCY_POLICY" in steps