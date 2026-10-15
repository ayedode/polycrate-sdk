from typing import Literal

AssistantSessionRequestKind = Literal["generic"]

ASSISTANT_SESSION_REQUEST_KIND_VALUES: set[AssistantSessionRequestKind] = {
    "generic",
}


def check_assistant_session_request_kind(value: str) -> AssistantSessionRequestKind:
    if value in ASSISTANT_SESSION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_REQUEST_KIND_VALUES!r}")
