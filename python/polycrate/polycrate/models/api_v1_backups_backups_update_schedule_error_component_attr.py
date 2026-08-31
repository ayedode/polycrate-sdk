from typing import Literal

ApiV1BackupsBackupsUpdateScheduleErrorComponentAttr = Literal["schedule"]

API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateScheduleErrorComponentAttr
] = {
    "schedule",
}


def check_api_v1_backups_backups_update_schedule_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateScheduleErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
