from typing import Literal

ProviderDetailState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

PROVIDER_DETAIL_STATE_VALUES: set[ProviderDetailState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_provider_detail_state(value: str) -> ProviderDetailState:
    if value in PROVIDER_DETAIL_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_STATE_VALUES!r}")
