from typing import Literal

WorkspaceEffectiveCriticalityType1 = Literal["high", "low", "medium"]

WORKSPACE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[WorkspaceEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_workspace_effective_criticality_type_1(value: str) -> WorkspaceEffectiveCriticalityType1:
    if value in WORKSPACE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
