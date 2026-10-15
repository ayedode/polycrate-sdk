from typing import Literal

PatchedAssistantSessionRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    PatchedAssistantSessionRequestCriticalityType3Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_assistant_session_request_criticality_type_3_type_1(
    value: str,
) -> PatchedAssistantSessionRequestCriticalityType3Type1:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
