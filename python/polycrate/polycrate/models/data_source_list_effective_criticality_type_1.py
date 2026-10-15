from typing import Literal

DataSourceListEffectiveCriticalityType1 = Literal["high", "low", "medium"]

DATA_SOURCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES: set[DataSourceListEffectiveCriticalityType1] = {
    "high",
    "low",
    "medium",
}


def check_data_source_list_effective_criticality_type_1(value: str) -> DataSourceListEffectiveCriticalityType1:
    if value in DATA_SOURCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_LIST_EFFECTIVE_CRITICALITY_TYPE_1_VALUES!r}"
    )
