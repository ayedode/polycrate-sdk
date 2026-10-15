from typing import Literal

DataSourceListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DATA_SOURCE_LIST_STATE_VALUES: set[DataSourceListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_data_source_list_state(value: str) -> DataSourceListState:
    if value in DATA_SOURCE_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_LIST_STATE_VALUES!r}")
