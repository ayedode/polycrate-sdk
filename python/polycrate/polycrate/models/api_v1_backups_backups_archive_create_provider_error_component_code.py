from typing import Literal

ApiV1BackupsBackupsArchiveCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_backups_backups_archive_create_provider_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateProviderErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
