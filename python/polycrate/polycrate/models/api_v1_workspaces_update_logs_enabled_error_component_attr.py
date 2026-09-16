from typing import Literal

ApiV1WorkspacesUpdateLogsEnabledErrorComponentAttr = Literal["logs_enabled"]

API_V1_WORKSPACES_UPDATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateLogsEnabledErrorComponentAttr
] = {
    "logs_enabled",
}


def check_api_v1_workspaces_update_logs_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateLogsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
