from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_backups_backup_schedules_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateNameErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
