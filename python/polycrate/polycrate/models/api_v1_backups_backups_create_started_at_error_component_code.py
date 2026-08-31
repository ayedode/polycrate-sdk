from typing import Literal

ApiV1BackupsBackupsCreateStartedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateStartedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_create_started_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateStartedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
