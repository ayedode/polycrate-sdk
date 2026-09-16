from typing import Literal

ApiV1WorkspacesRepairCreateLogsEnabledErrorComponentAttr = Literal["logs_enabled"]

API_V1_WORKSPACES_REPAIR_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesRepairCreateLogsEnabledErrorComponentAttr
] = {
    "logs_enabled",
}


def check_api_v1_workspaces_repair_create_logs_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesRepairCreateLogsEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_REPAIR_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_REPAIR_CREATE_LOGS_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
