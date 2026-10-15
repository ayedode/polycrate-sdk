from typing import Literal

DataSourceCriticalityType2Type1 = Literal["", "high", "low", "medium"]

DATA_SOURCE_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[DataSourceCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_data_source_criticality_type_2_type_1(value: str) -> DataSourceCriticalityType2Type1:
    if value in DATA_SOURCE_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}")
