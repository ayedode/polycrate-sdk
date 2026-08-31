from typing import Literal

ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_backups_backup_schedules_archive_create_slo_availability_error_component_code(
    value: str,
) -> ApiV1BackupsBackupSchedulesArchiveCreateSloAvailabilityErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
