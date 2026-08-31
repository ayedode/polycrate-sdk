from typing import Literal

ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_backups_backup_schedules_partial_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupSchedulesPartialUpdateTolerationsErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUP_SCHEDULES_PARTIAL_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
