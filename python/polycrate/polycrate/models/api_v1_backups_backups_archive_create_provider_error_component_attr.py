from typing import Literal

ApiV1BackupsBackupsArchiveCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_backups_backups_archive_create_provider_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateProviderErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
