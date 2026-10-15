from typing import Literal

PatchedDataSourceRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

PATCHED_DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[PatchedDataSourceRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_patched_data_source_request_criticality_type_3_type_1(
    value: str,
) -> PatchedDataSourceRequestCriticalityType3Type1:
    if value in PATCHED_DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
