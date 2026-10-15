from typing import Literal

AssistantSessionListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

ASSISTANT_SESSION_LIST_STATE_VALUES: set[AssistantSessionListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_assistant_session_list_state(value: str) -> AssistantSessionListState:
    if value in ASSISTANT_SESSION_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_LIST_STATE_VALUES!r}")
