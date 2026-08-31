from typing import Literal

ApiV1WorkspacesReloadCreateBackupEnabledErrorComponentAttr = Literal["backup_enabled"]

API_V1_WORKSPACES_RELOAD_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesReloadCreateBackupEnabledErrorComponentAttr
] = {
    "backup_enabled",
}


def check_api_v1_workspaces_reload_create_backup_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesReloadCreateBackupEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_RELOAD_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_RELOAD_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
