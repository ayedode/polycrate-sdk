from typing import Literal

DataSourceScope = Literal["system", "user"]

DATA_SOURCE_SCOPE_VALUES: set[DataSourceScope] = {
    "system",
    "user",
}


def check_data_source_scope(value: str) -> DataSourceScope:
    if value in DATA_SOURCE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_SCOPE_VALUES!r}")
