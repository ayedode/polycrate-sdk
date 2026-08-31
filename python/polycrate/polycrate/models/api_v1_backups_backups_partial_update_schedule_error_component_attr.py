from typing import Literal

ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentAttr = Literal["schedule"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentAttr
] = {
    "schedule",
}


def check_api_v1_backups_backups_partial_update_schedule_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateScheduleErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
