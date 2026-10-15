from typing import Literal

ProviderAccountListState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROVIDER_ACCOUNT_LIST_STATE_VALUES: set[ProviderAccountListState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_provider_account_list_state(value: str) -> ProviderAccountListState:
    if value in PROVIDER_ACCOUNT_LIST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_LIST_STATE_VALUES!r}")
