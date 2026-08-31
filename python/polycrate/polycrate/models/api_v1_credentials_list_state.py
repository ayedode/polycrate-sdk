from typing import Literal

ApiV1CredentialsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_CREDENTIALS_LIST_STATE_VALUES: set[ApiV1CredentialsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_credentials_list_state(value: str) -> ApiV1CredentialsListState:
    if value in API_V1_CREDENTIALS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_LIST_STATE_VALUES!r}")
