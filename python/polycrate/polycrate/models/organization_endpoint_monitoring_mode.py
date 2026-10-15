from typing import Literal

OrganizationEndpointMonitoringMode = Literal["auto", "manual"]

ORGANIZATION_ENDPOINT_MONITORING_MODE_VALUES: set[OrganizationEndpointMonitoringMode] = {
    "auto",
    "manual",
}


def check_organization_endpoint_monitoring_mode(value: str) -> OrganizationEndpointMonitoringMode:
    if value in ORGANIZATION_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ORGANIZATION_ENDPOINT_MONITORING_MODE_VALUES!r}")
