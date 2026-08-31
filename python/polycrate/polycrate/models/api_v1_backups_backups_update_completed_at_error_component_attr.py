from typing import Literal

ApiV1BackupsBackupsUpdateCompletedAtErrorComponentAttr = Literal["completed_at"]

API_V1_BACKUPS_BACKUPS_UPDATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateCompletedAtErrorComponentAttr
] = {
    "completed_at",
}


def check_api_v1_backups_backups_update_completed_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateCompletedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
