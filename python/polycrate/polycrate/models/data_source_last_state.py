from typing import Literal

DataSourceLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

DATA_SOURCE_LAST_STATE_VALUES: set[DataSourceLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_data_source_last_state(value: str) -> DataSourceLastState:
    if value in DATA_SOURCE_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {DATA_SOURCE_LAST_STATE_VALUES!r}")
