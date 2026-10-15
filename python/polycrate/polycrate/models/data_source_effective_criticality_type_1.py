from typing import Literal

DataSourceEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DATA_SOURCE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DataSourceEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_data_source_effective_criticality_type_1(value: str) -> DataSourceEffectiveCriticalityType1:
    if value in DATA_SOURCE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}")
