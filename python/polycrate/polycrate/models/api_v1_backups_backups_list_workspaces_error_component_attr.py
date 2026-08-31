from typing import Literal

ApiV1BackupsBackupsListWorkspacesErrorComponentAttr = Literal["workspaces"]

API_V1_BACKUPS_BACKUPS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListWorkspacesErrorComponentAttr
] = {
    "workspaces",
}


def check_api_v1_backups_backups_list_workspaces_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListWorkspacesErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_WORKSPACES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
