from typing import Literal

ApiV1BackupsBackupsCreateMetadataErrorComponentAttr = Literal["metadata"]

API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsCreateMetadataErrorComponentAttr
] = {
    "metadata",
}


def check_api_v1_backups_backups_create_metadata_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsCreateMetadataErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
