from typing import Literal

AssistantSessionCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ASSISTANT_SESSION_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AssistantSessionCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_assistant_session_criticality_type_3_type_1(value: str) -> AssistantSessionCriticalityType3Type1:
    if value in ASSISTANT_SESSION_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
