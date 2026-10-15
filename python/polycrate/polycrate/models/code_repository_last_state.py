from typing import Literal

CodeRepositoryLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CODE_REPOSITORY_LAST_STATE_VALUES: set[CodeRepositoryLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_code_repository_last_state(value: str) -> CodeRepositoryLastState:
    if value in CODE_REPOSITORY_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_LAST_STATE_VALUES!r}")
