from typing import Literal

PatchedWorkspaceRequestCriticalityType1 = Literal["", "high", "low", "medium"]

PATCHED_WORKSPACE_REQUEST_CRITICALITY_TYPE_1_VALUES: set[PatchedWorkspaceRequestCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_workspace_request_criticality_type_1(value: str) -> PatchedWorkspaceRequestCriticalityType1:
    if value in PATCHED_WORKSPACE_REQUEST_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_WORKSPACE_REQUEST_CRITICALITY_TYPE_1_VALUES!r}"
    )
