from typing import Literal

AssistantSessionKind = Literal["generic"]

ASSISTANT_SESSION_KIND_VALUES: set[AssistantSessionKind] = {
    "generic",
}


def check_assistant_session_kind(value: str) -> AssistantSessionKind:
    if value in ASSISTANT_SESSION_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_KIND_VALUES!r}")
