from typing import Literal

ProviderDetailRequestUnifiedApiAcrossLocations = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES: set[ProviderDetailRequestUnifiedApiAcrossLocations] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_unified_api_across_locations(
    value: str,
) -> ProviderDetailRequestUnifiedApiAcrossLocations:
    if value in PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES!r}"
    )
