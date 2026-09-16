from typing import Literal

ApiV1WorkspacesCheckCreateLogsEnabledErrorComponentAttr = Literal["logs_enabled"]

API_V1_WORKSPACES_CHECK_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateLogsEnabledErrorComponentAttr
] = {
    "logs_enabled",
}


def check_api_v1_workspaces_check_create_logs_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateLogsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
