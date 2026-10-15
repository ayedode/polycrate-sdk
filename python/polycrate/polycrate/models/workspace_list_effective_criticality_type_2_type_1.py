from typing import Literal

WorkspaceListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[WorkspaceListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_workspace_list_effective_criticality_type_2_type_1(value: str) -> WorkspaceListEffectiveCriticalityType2Type1:
    if value in WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
