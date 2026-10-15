from typing import Literal

ProjectDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROJECT_DETAIL_LAST_STATE_VALUES: set[ProjectDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_project_detail_last_state(value: str) -> ProjectDetailLastState:
    if value in PROJECT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROJECT_DETAIL_LAST_STATE_VALUES!r}")
