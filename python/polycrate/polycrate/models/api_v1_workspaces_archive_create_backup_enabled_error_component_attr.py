from typing import Literal

ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentAttr = Literal["backup_enabled"]

API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentAttr
] = {
    "backup_enabled",
}


def check_api_v1_workspaces_archive_create_backup_enabled_error_component_attr(
    value: str,
) -> ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentAttr:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
