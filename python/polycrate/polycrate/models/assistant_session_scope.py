from typing import Literal

AssistantSessionScope = Literal["system", "user"]

ASSISTANT_SESSION_SCOPE_VALUES: set[AssistantSessionScope] = {
    "system",
    "user",
}


def check_assistant_session_scope(value: str) -> AssistantSessionScope:
    if value in ASSISTANT_SESSION_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_SCOPE_VALUES!r}")
