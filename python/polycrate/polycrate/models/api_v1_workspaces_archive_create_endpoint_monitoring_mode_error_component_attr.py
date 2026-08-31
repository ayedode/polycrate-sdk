from typing import Literal

ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponentAttr = Literal["endpoint_monitoring_mode"]

API_V1_WORKSPACES_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponentAttr
] = {
    "endpoint_monitoring_mode",
}


def check_api_v1_workspaces_archive_create_endpoint_monitoring_mode_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateEndpointMonitoringModeErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_ENDPOINT_MONITORING_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
