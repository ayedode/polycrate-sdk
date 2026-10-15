from typing import Literal

PatchedRegionRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

PATCHED_REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[PatchedRegionRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_region_request_criticality_type_2_type_1(value: str) -> PatchedRegionRequestCriticalityType2Type1:
    if value in PATCHED_REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_REGION_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
