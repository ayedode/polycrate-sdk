from typing import Literal

AssistantSessionEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ASSISTANT_SESSION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AssistantSessionEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_assistant_session_effective_criticality_type_1(value: str) -> AssistantSessionEffectiveCriticalityType1:
    if value in ASSISTANT_SESSION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
