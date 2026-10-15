from typing import Literal

ProviderAccountDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROVIDER_ACCOUNT_DETAIL_LAST_STATE_VALUES: set[ProviderAccountDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_provider_account_detail_last_state(value: str) -> ProviderAccountDetailLastState:
    if value in PROVIDER_ACCOUNT_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_ACCOUNT_DETAIL_LAST_STATE_VALUES!r}")
