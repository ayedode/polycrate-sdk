from typing import Literal

AssistantSessionState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ASSISTANT_SESSION_STATE_VALUES: set[AssistantSessionState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_assistant_session_state(value: str) -> AssistantSessionState:
    if value in ASSISTANT_SESSION_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_STATE_VALUES!r}")
