from typing import Literal

ProjectListEffectiveCriticalityType3Type1 = Literal["high", "low", "medium"]

PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProjectListEffectiveCriticalityType3Type1] = {
    "high",
    "low",
    "medium",
}


def check_project_list_effective_criticality_type_3_type_1(value: str) -> ProjectListEffectiveCriticalityType3Type1:
    if value in PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
