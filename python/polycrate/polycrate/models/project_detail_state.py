from typing import Literal

ProjectDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROJECT_DETAIL_STATE_VALUES: set[ProjectDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_project_detail_state(value: str) -> ProjectDetailState:
    if value in PROJECT_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_STATE_VALUES!r}")
