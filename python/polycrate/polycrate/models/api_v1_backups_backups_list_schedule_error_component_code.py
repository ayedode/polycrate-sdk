from typing import Literal

ApiV1BackupsBackupsListScheduleErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsListScheduleErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_backups_backups_list_schedule_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsListScheduleErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
