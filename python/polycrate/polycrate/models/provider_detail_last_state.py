from typing import Literal

ProviderDetailLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROVIDER_DETAIL_LAST_STATE_VALUES: set[ProviderDetailLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_provider_detail_last_state(value: str) -> ProviderDetailLastState:
    if value in PROVIDER_DETAIL_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_LAST_STATE_VALUES!r}")
