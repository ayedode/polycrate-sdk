from typing import Literal

ApiV1ProviderAccountsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_VALUES: set[ApiV1ProviderAccountsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1_provider_accounts_list_state_not(value: str) -> ApiV1ProviderAccountsListStateNot:
    if value in API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_LIST_STATE_NOT_VALUES!r}")
