from typing import Literal

PopCatalogTier = Literal["tier1", "tier2", "tier3", "tier4"]

POP_CATALOG_TIER_VALUES: set[PopCatalogTier] = {
    "tier1",
    "tier2",
    "tier3",
    "tier4",
}


def check_pop_catalog_tier(value: str) -> PopCatalogTier:
    if value in POP_CATALOG_TIER_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POP_CATALOG_TIER_VALUES!r}")
