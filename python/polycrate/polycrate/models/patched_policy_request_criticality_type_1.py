from typing import Literal

PatchedPolicyRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedPolicyRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_policy_request_criticality_type_1(value: str) -> PatchedPolicyRequestCriticalityType1:
    if value in PATCHED_POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POLICY_REQUEST_CRITICALITY_TYPE_1_VALUES!r}")
