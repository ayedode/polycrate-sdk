from typing import Literal

ApiV1ProvidersListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PROVIDERS_LIST_STATE_VALUES: set[ApiV1ProvidersListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_providers_list_state(value: str) -> ApiV1ProvidersListState:
    if value in API_V1_PROVIDERS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_LIST_STATE_VALUES!r}")
