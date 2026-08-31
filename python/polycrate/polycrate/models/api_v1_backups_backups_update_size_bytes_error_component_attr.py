from typing import Literal

ApiV1BackupsBackupsUpdateSizeBytesErrorComponentAttr = Literal["size_bytes"]

API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsUpdateSizeBytesErrorComponentAttr
] = {
    "size_bytes",
}


def check_api_v1_backups_backups_update_size_bytes_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsUpdateSizeBytesErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
