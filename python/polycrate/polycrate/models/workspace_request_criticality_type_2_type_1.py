from typing import Literal

WorkspaceRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

WORKSPACE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[WorkspaceRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_workspace_request_criticality_type_2_type_1(value: str) -> WorkspaceRequestCriticalityType2Type1:
    if value in WORKSPACE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
