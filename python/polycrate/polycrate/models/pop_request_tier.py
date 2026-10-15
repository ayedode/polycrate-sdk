from typing import Literal

PopRequestTier = Literal["", "tier1", "tier2", "tier3", "tier4"]

POP_REQUEST_TIER_VALUES: set[PopRequestTier] = {
    "",
    "tier1",
    "tier2",
    "tier3",
    "tier4",
}


def check_pop_request_tier(value: str) -> PopRequestTier:
    if value in POP_REQUEST_TIER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_REQUEST_TIER_VALUES!r}")
