from typing import Literal

AssistantSessionStatusEnum = Literal["closed", "open"]

ASSISTANT_SESSION_STATUS_ENUM_VALUES: set[AssistantSessionStatusEnum] = {
    "closed",
    "open",
}


def check_assistant_session_status_enum(value: str) -> AssistantSessionStatusEnum:
    if value in ASSISTANT_SESSION_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_STATUS_ENUM_VALUES!r}")
