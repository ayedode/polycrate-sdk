from typing import Literal

CodeRepositoryListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

CODE_REPOSITORY_LIST_STATE_VALUES: set[CodeRepositoryListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_code_repository_list_state(value: str) -> CodeRepositoryListState:
    if value in CODE_REPOSITORY_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CODE_REPOSITORY_LIST_STATE_VALUES!r}")
