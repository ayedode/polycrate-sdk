from typing import Literal

SecretManagerListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

SECRET_MANAGER_LIST_STATE_VALUES: set[SecretManagerListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_secret_manager_list_state(value: str) -> SecretManagerListState:
    if value in SECRET_MANAGER_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_LIST_STATE_VALUES!r}")
