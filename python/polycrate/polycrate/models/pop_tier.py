from typing import Literal

PopTier = Literal["", "tier1", "tier2", "tier3", "tier4"]

POP_TIER_VALUES: set[PopTier] = {
    "",
    "tier1",
    "tier2",
    "tier3",
    "tier4",
}


def check_pop_tier(value: str) -> PopTier:
    if value in POP_TIER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_TIER_VALUES!r}")
