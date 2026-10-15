from typing import Literal

DataSourceCriticalityType1 = Literal["", "high", "low", "medium"]

DATA_SOURCE_CRITICALITY_TYPE_1_VALUES: set[DataSourceCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_data_source_criticality_type_1(value: str) -> DataSourceCriticalityType1:
    if value in DATA_SOURCE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_CRITICALITY_TYPE_1_VALUES!r}")
