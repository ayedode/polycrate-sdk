from typing import Literal

CodeRepositoryState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CODE_REPOSITORY_STATE_VALUES: set[CodeRepositoryState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_code_repository_state(value: str) -> CodeRepositoryState:
    if value in CODE_REPOSITORY_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_STATE_VALUES!r}")
