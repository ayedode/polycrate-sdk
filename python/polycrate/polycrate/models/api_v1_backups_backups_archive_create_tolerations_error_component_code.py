from typing import Literal

ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_archive_create_tolerations_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateTolerationsErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_TOLERATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
