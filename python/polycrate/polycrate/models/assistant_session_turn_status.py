from typing import Literal

AssistantSessionTurnStatus = Literal["idle", "queued", "running"]

ASSISTANT_SESSION_TURN_STATUS_VALUES: set[AssistantSessionTurnStatus] = {
    "idle",
    "queued",
    "running",
}


def check_assistant_session_turn_status(value: str) -> AssistantSessionTurnStatus:
    if value in ASSISTANT_SESSION_TURN_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_TURN_STATUS_VALUES!r}")
