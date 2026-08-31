from typing import Literal

ApiV1BackupsBackupsUpdateScheduleErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateScheduleErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_backups_backups_update_schedule_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateScheduleErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
