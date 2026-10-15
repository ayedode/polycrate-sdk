from typing import Literal

WorkspaceCriticalityType1 = Literal["", "high", "low", "medium"]

WORKSPACE_CRITICALITY_TYPE_1_VALUES: set[WorkspaceCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_workspace_criticality_type_1(value: str) -> WorkspaceCriticalityType1:
    if value in WORKSPACE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_CRITICALITY_TYPE_1_VALUES!r}")
