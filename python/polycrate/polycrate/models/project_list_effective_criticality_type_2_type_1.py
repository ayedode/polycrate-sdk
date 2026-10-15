from typing import Literal

ProjectListEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProjectListEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_project_list_effective_criticality_type_2_type_1(value: str) -> ProjectListEffectiveCriticalityType2Type1:
    if value in PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_LIST_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
