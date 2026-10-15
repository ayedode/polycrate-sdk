from typing import Literal

ProviderDetailUnifiedApiAcrossLocations = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_UNIFIED_API_ACROSS_LOCATIONS_VALUES: set[ProviderDetailUnifiedApiAcrossLocations] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_unified_api_across_locations(value: str) -> ProviderDetailUnifiedApiAcrossLocations:
    if value in PROVIDER_DETAIL_UNIFIED_API_ACROSS_LOCATIONS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_UNIFIED_API_ACROSS_LOCATIONS_VALUES!r}"
    )
