from typing import Literal

ApiV1BackupsBackupsUpdateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_BACKUPS_BACKUPS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_backups_backups_update_metadata_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateMetadataErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
