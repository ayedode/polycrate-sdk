from typing import Literal

ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentCode = Literal["invalid", "null"]

API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_workspaces_archive_create_backup_enabled_error_component_code(
    value: str,
) -> ApiV1WorkspacesArchiveCreateBackupEnabledErrorComponentCode:
    if value in API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_WORKSPACES_ARCHIVE_CREATE_BACKUP_ENABLED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
