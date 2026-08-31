from typing import Literal

WorkspaceEndpointMonitoringModeEnum = Literal["auto", "organization_only", "pop_only", "workspace_only"]

WORKSPACE_ENDPOINT_MONITORING_MODE_ENUM_VALUES: set[WorkspaceEndpointMonitoringModeEnum] = {
    "auto",
    "organization_only",
    "pop_only",
    "workspace_only",
}


def check_workspace_endpoint_monitoring_mode_enum(value: str) -> WorkspaceEndpointMonitoringModeEnum:
    if value in WORKSPACE_ENDPOINT_MONITORING_MODE_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {WORKSPACE_ENDPOINT_MONITORING_MODE_ENUM_VALUES!r}")
