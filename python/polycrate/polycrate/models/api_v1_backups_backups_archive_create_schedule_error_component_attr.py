from typing import Literal

ApiV1BackupsBackupsArchiveCreateScheduleErrorComponentAttr = Literal["schedule"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateScheduleErrorComponentAttr
] = {
    "schedule",
}


def check_api_v1_backups_backups_archive_create_schedule_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateScheduleErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_SCHEDULE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
