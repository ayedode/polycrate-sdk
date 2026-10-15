from typing import Literal

AssistantSessionRequestCriticalityType1 = Literal["", "high", "low", "medium"]

ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES: set[AssistantSessionRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_assistant_session_request_criticality_type_1(value: str) -> AssistantSessionRequestCriticalityType1:
    if value in ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
