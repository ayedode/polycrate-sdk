from typing import Literal

ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_backups_backup_schedules_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
