from typing import Literal

OrganizationEndpointMonitoringModeEnum = Literal["auto", "manual"]

ORGANIZATION_ENDPOINT_MONITORING_MODE_ENUM_VALUES: set[OrganizationEndpointMonitoringModeEnum] = {
    "auto",
    "manual",
}


def check_organization_endpoint_monitoring_mode_enum(value: str) -> OrganizationEndpointMonitoringModeEnum:
    if value in ORGANIZATION_ENDPOINT_MONITORING_MODE_ENUM_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_ENDPOINT_MONITORING_MODE_ENUM_VALUES!r}"
    )
