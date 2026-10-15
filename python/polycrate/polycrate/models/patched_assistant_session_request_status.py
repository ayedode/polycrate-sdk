from typing import Literal

PatchedAssistantSessionRequestStatus = Literal["closed", "open"]

PATCHED_ASSISTANT_SESSION_REQUEST_STATUS_VALUES: set[PatchedAssistantSessionRequestStatus] = {
    "closed",
    "open",
}


def check_patched_assistant_session_request_status(value: str) -> PatchedAssistantSessionRequestStatus:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_STATUS_VALUES!r}")
