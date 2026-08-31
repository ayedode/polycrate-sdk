from typing import Literal

ApiV1BackupsBackupsUpdateStartedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateStartedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_update_started_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateStartedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_STARTED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
