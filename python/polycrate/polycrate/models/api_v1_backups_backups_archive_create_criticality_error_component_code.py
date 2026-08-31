from typing import Literal

ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_backups_backups_archive_create_criticality_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateCriticalityErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
