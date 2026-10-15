from typing import Literal

PatchedAssistantSessionRequestKind = Literal["generic"]

PATCHED_ASSISTANT_SESSION_REQUEST_KIND_VALUES: set[PatchedAssistantSessionRequestKind] = {
    "generic",
}


def check_patched_assistant_session_request_kind(value: str) -> PatchedAssistantSessionRequestKind:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_KIND_VALUES!r}")
