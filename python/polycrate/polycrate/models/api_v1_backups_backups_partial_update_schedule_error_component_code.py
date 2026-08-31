from typing import Literal

ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_backups_backups_partial_update_schedule_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
