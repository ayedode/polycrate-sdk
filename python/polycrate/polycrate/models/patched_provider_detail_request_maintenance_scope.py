from typing import Literal

PatchedProviderDetailRequestMaintenanceScope = Literal["", "both", "object", "system", "unknown"]

PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES: set[PatchedProviderDetailRequestMaintenanceScope] = {
    "",
    "both",
    "object",
    "system",
    "unknown",
}


def check_patched_provider_detail_request_maintenance_scope(value: str) -> PatchedProviderDetailRequestMaintenanceScope:
    if value in PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES!r}"
    )
