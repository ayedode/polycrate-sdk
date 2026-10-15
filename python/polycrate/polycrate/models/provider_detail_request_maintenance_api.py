from typing import Literal

ProviderDetailRequestMaintenanceApi = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES: set[ProviderDetailRequestMaintenanceApi] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_maintenance_api(value: str) -> ProviderDetailRequestMaintenanceApi:
    if value in PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_MAINTENANCE_API_VALUES!r}")
