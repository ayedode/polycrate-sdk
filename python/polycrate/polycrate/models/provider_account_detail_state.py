from typing import Literal

ProviderAccountDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROVIDER_ACCOUNT_DETAIL_STATE_VALUES: set[ProviderAccountDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_provider_account_detail_state(value: str) -> ProviderAccountDetailState:
    if value in PROVIDER_ACCOUNT_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_STATE_VALUES!r}")
