from typing import Literal

WorkspaceTemplateListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

WORKSPACE_TEMPLATE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[
    WorkspaceTemplateListEffectiveCriticalityType3Type1
] = {
    "high",
    "low",
    "medium",
}


def check_workspace_template_list_effective_criticality_type_3_type_1(
    value: str,
) -> WorkspaceTemplateListEffectiveCriticalityType3Type1:
    if value in WORKSPACE_TEMPLATE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_TEMPLATE_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
