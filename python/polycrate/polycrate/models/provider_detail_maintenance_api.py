from typing import Literal

ProviderDetailMaintenanceApi = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_MAINTENANCE_API_VALUES: set[ProviderDetailMaintenanceApi] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_maintenance_api(value: str) -> ProviderDetailMaintenanceApi:
    if value in PROVIDER_DETAIL_MAINTENANCE_API_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_MAINTENANCE_API_VALUES!r}")
