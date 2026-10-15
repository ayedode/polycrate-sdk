from typing import Literal

PatchedAssistantSessionRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedAssistantSessionRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_assistant_session_request_criticality_type_1(
    value: str,
) -> PatchedAssistantSessionRequestCriticalityType1:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
