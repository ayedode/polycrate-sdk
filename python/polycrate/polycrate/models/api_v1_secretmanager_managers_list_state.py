from typing import Literal

ApiV1SecretmanagerManagersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_VALUES: set[ApiV1SecretmanagerManagersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_secretmanager_managers_list_state(value: str) -> ApiV1SecretmanagerManagersListState:
    if value in API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_LIST_STATE_VALUES!r}")
