from typing import Literal

ApiV1BackupsBackupsListScheduleErrorComponentAttr = Literal["schedule"]

API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsListScheduleErrorComponentAttr
] = {
    "schedule",
}


def check_api_v1_backups_backups_list_schedule_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsListScheduleErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_LIST_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
