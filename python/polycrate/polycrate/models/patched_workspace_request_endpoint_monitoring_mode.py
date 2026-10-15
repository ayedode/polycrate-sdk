from typing import Literal

PatchedWorkspaceRequestEndpointMonitoringMode = Literal["auto", "organization_only", "pop_only", "workspace_only"]

PATCHED_WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES: set[PatchedWorkspaceRequestEndpointMonitoringMode] = {
    "auto",
    "organization_only",
    "pop_only",
    "workspace_only",
}


def check_patched_workspace_request_endpoint_monitoring_mode(
    value: str,
) -> PatchedWorkspaceRequestEndpointMonitoringMode:
    if value in PATCHED_WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PATCHED_WORKSPACE_REQUEST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
