from typing import Literal

PatchedPopRequestTier = Literal["", "tier1", "tier2", "tier3", "tier4"]

PATCHED_POP_REQUEST_TIER_VALUES: set[PatchedPopRequestTier] = {
    "",
    "tier1",
    "tier2",
    "tier3",
    "tier4",
}


def check_patched_pop_request_tier(value: str) -> PatchedPopRequestTier:
    if value in PATCHED_POP_REQUEST_TIER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PATCHED_POP_REQUEST_TIER_VALUES!r}")
