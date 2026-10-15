from typing import Literal

AssistantSessionRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[AssistantSessionRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_assistant_session_request_criticality_type_3_type_1(
    value: str,
) -> AssistantSessionRequestCriticalityType3Type1:
    if value in ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
