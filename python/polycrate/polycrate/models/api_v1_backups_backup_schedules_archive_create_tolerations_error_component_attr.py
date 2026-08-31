from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_backups_backup_schedules_archive_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateTolerationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
