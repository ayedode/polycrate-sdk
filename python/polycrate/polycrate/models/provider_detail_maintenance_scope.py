from typing import Literal

ProviderDetailMaintenanceScope = Literal["", "both", "object", "system", "unknown"]

PROVIDER_DETAIL_MAINTENANCE_SCOPE_VALUES: set[ProviderDetailMaintenanceScope] = {
    "",
    "both",
    "object",
    "system",
    "unknown",
}


def check_provider_detail_maintenance_scope(value: str) -> ProviderDetailMaintenanceScope:
    if value in PROVIDER_DETAIL_MAINTENANCE_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_MAINTENANCE_SCOPE_VALUES!r}")
