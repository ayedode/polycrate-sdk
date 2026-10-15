from typing import Literal

PatchedProviderDetailRequestMaintenanceApi = Literal["no", "planned", "unknown", "yes"]

PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES: set[PatchedProviderDetailRequestMaintenanceApi] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_patched_provider_detail_request_maintenance_api(value: str) -> PatchedProviderDetailRequestMaintenanceApi:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES!r}"
    )
