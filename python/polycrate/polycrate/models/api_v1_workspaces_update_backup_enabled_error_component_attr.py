from typing import Literal

ApiV1WorkspacesUpdateBackupEnabledErrorComponentAttr = Literal["backup_enabled"]

API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesUpdateBackupEnabledErrorComponentAttr
] = {
    "backup_enabled",
}


def check_api_v1_workspaces_update_backup_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesUpdateBackupEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_UPDATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
