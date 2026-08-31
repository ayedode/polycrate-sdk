from typing import Literal

ApiV1ProviderAccountsListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PROVIDER_ACCOUNTS_LIST_STATE_VALUES: set[ApiV1ProviderAccountsListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_provider_accounts_list_state(value: str) -> ApiV1ProviderAccountsListState:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_STATE_VALUES!r}")
