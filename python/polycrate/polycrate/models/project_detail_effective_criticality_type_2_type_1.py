from typing import Literal

ProjectDetailEffectiveCriticalityType2Type1 = Literal["high", "low", "medium"]

PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProjectDetailEffectiveCriticalityType2Type1] = {
    "high",
    "low",
    "medium",
}


def check_project_detail_effective_criticality_type_2_type_1(value: str) -> ProjectDetailEffectiveCriticalityType2Type1:
    if value in PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_EFFECTIVE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
