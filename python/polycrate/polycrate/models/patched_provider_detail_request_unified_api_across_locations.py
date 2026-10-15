from typing import Literal

PatchedProviderDetailRequestUnifiedApiAcrossLocations = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES: set[
    PatchedProviderDetailRequestUnifiedApiAcrossLocations
] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_unified_api_across_locations(
    value: str,
) -> PatchedProviderDetailRequestUnifiedApiAcrossLocations:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_UNIFIED_API_ACROSS_LOCATIONS_VALUES!r}"
    )
