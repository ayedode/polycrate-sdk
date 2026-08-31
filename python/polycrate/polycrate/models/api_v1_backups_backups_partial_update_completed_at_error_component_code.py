from typing import Literal

ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_backups_backups_partial_update_completed_at_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateCompletedAtErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_COMPLETED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
