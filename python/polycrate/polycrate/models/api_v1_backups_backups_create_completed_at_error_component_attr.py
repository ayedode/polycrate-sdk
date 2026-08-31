from typing import Literal

ApiV1BackupsBackupsCreateCompletedAtErrorComponentAttr = Literal["completed_at"]

API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateCompletedAtErrorComponentAttr
] = {
    "completed_at",
}


def check_api_v1_backups_backups_create_completed_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateCompletedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
