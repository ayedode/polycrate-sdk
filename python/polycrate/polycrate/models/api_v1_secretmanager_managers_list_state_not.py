from typing import Literal

ApiV1SecretmanagerManagersListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_NOT_VALUES: set[ApiV1SecretmanagerManagersListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_secretmanager_managers_list_state_not(value: str) -> ApiV1SecretmanagerManagersListStateNot:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_NOT_VALUES!r}"
    )
