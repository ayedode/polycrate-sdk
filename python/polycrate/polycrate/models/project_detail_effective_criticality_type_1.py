from typing import Literal

ProjectDetailEffectiveCriticalityType1 = Literal["high", "low", "medium"]

PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[ProjectDetailEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_project_detail_effective_criticality_type_1(value: str) -> ProjectDetailEffectiveCriticalityType1:
    if value in PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
