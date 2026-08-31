from typing import Literal

ApiV1WorkspacesListEndpointMonitoringMode = Literal["auto", "manual"]

API_V1_WORKSPACES_LIST_ENDPOINT_MONITORING_MODE_VALUES: set[ApiV1WorkspacesListEndpointMonitoringMode] = {
    "auto",
    "manual",
}


def check_api_v1_workspaces_list_endpoint_monitoring_mode(value: str) -> ApiV1WorkspacesListEndpointMonitoringMode:
    if value in API_V1_WORKSPACES_LIST_ENDPOINT_MONITORING_MODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LIST_ENDPOINT_MONITORING_MODE_VALUES!r}"
    )
