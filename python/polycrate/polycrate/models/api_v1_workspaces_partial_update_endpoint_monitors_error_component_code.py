from typing import Literal

ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponentCode = Literal[
    "does_not_exist", "incorrect_type", "not_a_list", "null"
]

API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
    "not_a_list",
    "null",
}


def check_api_v1_workspaces_partial_update_endpoint_monitors_error_component_code(
    value: str,
) -> ApiV1WorkspacesPartialUpdateEndpointMonitorsErrorComponentCode:
    if value in API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_PARTIAL_UPDATE_ENDPOINT_MONITORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
