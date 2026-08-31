from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1_backups_backup_schedules_archive_create_platform_service_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreatePlatformServiceErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
