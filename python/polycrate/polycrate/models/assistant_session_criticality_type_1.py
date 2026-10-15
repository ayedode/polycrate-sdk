from typing import Literal

AssistantSessionCriticalityType1 = Literal["", "high", "low", "medium"]

ASSISTANT_SESSION_CRITICALITY_TYPE_1_VALUES: set[AssistantSessionCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_assistant_session_criticality_type_1(value: str) -> AssistantSessionCriticalityType1:
    if value in ASSISTANT_SESSION_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_CRITICALITY_TYPE_1_VALUES!r}")
