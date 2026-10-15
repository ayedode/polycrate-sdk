from typing import Literal

PatchedSecretManagerRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedSecretManagerRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_secret_manager_request_criticality_type_1(value: str) -> PatchedSecretManagerRequestCriticalityType1:
    if value in PATCHED_SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_SECRET_MANAGER_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
