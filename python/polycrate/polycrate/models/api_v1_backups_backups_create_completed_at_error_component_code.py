from typing import Literal

ApiV1BackupsBackupsCreateCompletedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateCompletedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_create_completed_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateCompletedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
