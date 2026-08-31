from typing import Literal

ApiV1BackupsBackupsArchiveCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsArchiveCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_backups_backups_archive_create_metadata_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsArchiveCreateMetadataErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_ARCHIVE_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
