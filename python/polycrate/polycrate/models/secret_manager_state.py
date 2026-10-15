from typing import Literal

SecretManagerState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

SECRET_MANAGER_STATE_VALUES: set[SecretManagerState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_secret_manager_state(value: str) -> SecretManagerState:
    if value in SECRET_MANAGER_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_STATE_VALUES!r}")
