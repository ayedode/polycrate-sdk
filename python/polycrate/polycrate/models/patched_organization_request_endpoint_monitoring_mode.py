from typing import Literal

PatchedOrganizationRequestEndpointMonitoringMode = Literal["auto", "manual"]

PATCHED_ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES: set[PatchedOrganizationRequestEndpointMonitoringMode] = {
    "auto",
    "manual",
}


def check_patched_organization_request_endpoint_monitoring_mode(
    value: str,
) -> PatchedOrganizationRequestEndpointMonitoringMode:
    if value in PATCHED_ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_ORGANIZATION_REQUEST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
