from typing import Literal

ApiV1WorkspacesLogsReloadCreateNameErrorComponentAttr = Literal["name"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_workspaces_logs_reload_create_name_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateNameErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
