from typing import Literal

ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_workspaces_logs_reload_create_endpoint_monitors_error_component_code(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateEndpointMonitorsErrorComponentCode:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
