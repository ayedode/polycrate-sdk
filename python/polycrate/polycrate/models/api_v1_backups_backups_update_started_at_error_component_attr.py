from typing import Literal

ApiV1BackupsBackupsUpdateStartedAtErrorComponentAttr = Literal["started_at"]

API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateStartedAtErrorComponentAttr
] = {
    "started_at",
}


def check_api_v1_backups_backups_update_started_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateStartedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
