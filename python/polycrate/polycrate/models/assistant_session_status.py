from typing import Literal

AssistantSessionStatus = Literal["closed", "open"]

ASSISTANT_SESSION_STATUS_VALUES: set[AssistantSessionStatus] = {
    "closed",
    "open",
}


def check_assistant_session_status(value: str) -> AssistantSessionStatus:
    if value in ASSISTANT_SESSION_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_STATUS_VALUES!r}")
