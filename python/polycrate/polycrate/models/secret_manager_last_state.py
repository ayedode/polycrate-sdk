from typing import Literal

SecretManagerLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

SECRET_MANAGER_LAST_STATE_VALUES: set[SecretManagerLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_secret_manager_last_state(value: str) -> SecretManagerLastState:
    if value in SECRET_MANAGER_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_LAST_STATE_VALUES!r}")
