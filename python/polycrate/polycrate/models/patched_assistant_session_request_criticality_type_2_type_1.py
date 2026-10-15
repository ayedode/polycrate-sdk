from typing import Literal

PatchedAssistantSessionRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[
    PatchedAssistantSessionRequestCriticalityType2Type1
] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_assistant_session_request_criticality_type_2_type_1(
    value: str,
) -> PatchedAssistantSessionRequestCriticalityType2Type1:
    if value in PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ASSISTANT_SESSION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
