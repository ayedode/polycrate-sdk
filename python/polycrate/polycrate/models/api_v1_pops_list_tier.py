from typing import Literal

ApiV1PopsListTier = Literal["tier1", "tier2", "tier3", "tier4"]

API_V1_POPS_LIST_TIER_VALUES: set[ApiV1PopsListTier] = {
    "tier1",
    "tier2",
    "tier3",
    "tier4",
}


def check_api_v1_pops_list_tier(value: str) -> ApiV1PopsListTier:
    if value in API_V1_POPS_LIST_TIER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1_POPS_LIST_TIER_VALUES!r}")
