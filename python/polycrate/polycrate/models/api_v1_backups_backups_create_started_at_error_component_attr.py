from typing import Literal

ApiV1BackupsBackupsCreateStartedAtErrorComponentAttr = Literal["started_at"]

API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateStartedAtErrorComponentAttr
] = {
    "started_at",
}


def check_api_v1_backups_backups_create_started_at_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateStartedAtErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
