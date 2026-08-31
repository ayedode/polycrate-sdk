from typing import Literal

ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_workspaces_logs_reload_create_archived_error_component_attr(
    value: str,
) -> ApiV1WorkspacesLogsReloadCreateArchivedErrorComponentAttr:
    if value in API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_LOGS_RELOAD_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
