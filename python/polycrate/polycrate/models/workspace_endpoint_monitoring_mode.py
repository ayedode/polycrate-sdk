from typing import Literal

WorkspaceEndpointMonitoringMode = Literal["auto", "organization_only", "pop_only", "workspace_only"]

WORKSPACE_ENDPOINT_MONITORING_MODE_VALUES: set[WorkspaceEndpointMonitoringMode] = {
    "auto",
    "organization_only",
    "pop_only",
    "workspace_only",
}


def check_workspace_endpoint_monitoring_mode(value: str) -> WorkspaceEndpointMonitoringMode:
    if value in WORKSPACE_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_ENDPOINT_MONITORING_MODE_VALUES!r}")
