from typing import Literal

DataSourceState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DATA_SOURCE_STATE_VALUES: set[DataSourceState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_data_source_state(value: str) -> DataSourceState:
    if value in DATA_SOURCE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_STATE_VALUES!r}")
