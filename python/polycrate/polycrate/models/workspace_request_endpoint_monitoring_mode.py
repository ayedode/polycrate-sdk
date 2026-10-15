from typing import Literal

WorkspaceRequestEndpointMonitoringMode = Literal["auto", "organization_only", "pop_only", "workspace_only"]

WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES: set[WorkspaceRequestEndpointMonitoringMode] = {
    "auto",
    "organization_only",
    "pop_only",
    "workspace_only",
}


def check_workspace_request_endpoint_monitoring_mode(value: str) -> WorkspaceRequestEndpointMonitoringMode:
    if value in WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
