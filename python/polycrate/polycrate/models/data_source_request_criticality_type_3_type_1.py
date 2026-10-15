from typing import Literal

DataSourceRequestCriticalityType3Type1 = Literal["", "high", "low", "medium"]

DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES: set[DataSourceRequestCriticalityType3Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_data_source_request_criticality_type_3_type_1(value: str) -> DataSourceRequestCriticalityType3Type1:
    if value in DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_REQUEST_CRITICALITY_TYPE_3_TYPE_1_VALUES!r}"
    )
