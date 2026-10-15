from typing import Literal

ProviderDetailRequestMaintenanceScope = Literal["", "both", "object", "system", "unknown"]

PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES: set[ProviderDetailRequestMaintenanceScope] = {
    "",
    "both",
    "object",
    "system",
    "unknown",
}


def check_provider_detail_request_maintenance_scope(value: str) -> ProviderDetailRequestMaintenanceScope:
    if value in PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_MAINTENANCE_SCOPE_VALUES!r}")
