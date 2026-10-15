from typing import Literal

OrganizationRequestEndpointMonitoringMode = Literal["auto", "manual"]

ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES: set[OrganizationRequestEndpointMonitoringMode] = {
    "auto",
    "manual",
}


def check_organization_request_endpoint_monitoring_mode(value: str) -> OrganizationRequestEndpointMonitoringMode:
    if value in ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
