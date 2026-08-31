from typing import Literal

ApiV1BackupsBackupsArchiveCreateExpirationErrorComponentAttr = Literal["expiration"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateExpirationErrorComponentAttr
] = {
    "expiration",
}


def check_api_v1_backups_backups_archive_create_expiration_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateExpirationErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_EXPIRATION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
