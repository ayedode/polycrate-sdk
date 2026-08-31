from typing import Literal

ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentAttr = Literal["backup_enabled"]

API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentAttr
] = {
    "backup_enabled",
}


def check_api_v1_workspaces_check_create_backup_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesCheckCreateBackupEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_CHECK_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
