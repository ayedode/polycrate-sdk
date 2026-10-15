from typing import Literal

ProjectDetailCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PROJECT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[ProjectDetailCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_project_detail_criticality_type_2_type_1(value: str) -> ProjectDetailCriticalityType2Type1:
    if value in PROJECT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
