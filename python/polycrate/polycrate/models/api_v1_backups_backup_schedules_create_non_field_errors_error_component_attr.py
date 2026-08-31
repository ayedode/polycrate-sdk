from typing import Literal

ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_backups_backup_schedules_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
