from typing import Literal

RegionRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[RegionRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_region_request_criticality_type_2_type_1(value: str) -> RegionRequestCriticalityType2Type1:
    if value in REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
