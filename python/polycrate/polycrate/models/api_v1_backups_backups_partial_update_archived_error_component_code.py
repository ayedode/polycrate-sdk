from typing import Literal

ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
