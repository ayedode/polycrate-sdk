from typing import Literal

AssistantSessionLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ASSISTANT_SESSION_LAST_STATE_VALUES: set[AssistantSessionLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_assistant_session_last_state(value: str) -> AssistantSessionLastState:
    if value in ASSISTANT_SESSION_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_LAST_STATE_VALUES!r}")
