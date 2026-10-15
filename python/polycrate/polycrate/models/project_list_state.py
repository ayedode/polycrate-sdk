from typing import Literal

ProjectListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROJECT_LIST_STATE_VALUES: set[ProjectListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_project_list_state(value: str) -> ProjectListState:
    if value in PROJECT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_LIST_STATE_VALUES!r}")
