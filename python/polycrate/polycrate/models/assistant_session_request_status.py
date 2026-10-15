from typing import Literal

AssistantSessionRequestStatus = Literal["closed", "open"]

ASSISTANT_SESSION_REQUEST_STATUS_VALUES: set[AssistantSessionRequestStatus] = {
    "closed",
    "open",
}


def check_assistant_session_request_status(value: str) -> AssistantSessionRequestStatus:
    if value in ASSISTANT_SESSION_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_REQUEST_STATUS_VALUES!r}")
