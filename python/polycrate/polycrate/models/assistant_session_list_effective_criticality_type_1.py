from typing import Literal

AssistantSessionListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

ASSISTANT_SESSION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[AssistantSessionListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_assistant_session_list_effective_criticality_type_1(
    value: str,
) -> AssistantSessionListEffectiveCriticalityType1:
    if value in ASSISTANT_SESSION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
