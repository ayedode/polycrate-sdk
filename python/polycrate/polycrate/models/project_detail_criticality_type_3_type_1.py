from typing import Literal

ProjectDetailCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PROJECT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[ProjectDetailCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_project_detail_criticality_type_3_type_1(value: str) -> ProjectDetailCriticalityType3Type1:
    if value in PROJECT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}")
