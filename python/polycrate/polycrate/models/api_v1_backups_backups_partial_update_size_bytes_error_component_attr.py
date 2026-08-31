from typing import Literal

ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponentAttr = Literal["size_bytes"]

API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponentAttr
] = {
    "size_bytes",
}


def check_api_v1_backups_backups_partial_update_size_bytes_error_component_attr(
    value: str,
) -> ApiV1BackupsBackupsPartialUpdateSizeBytesErrorComponentAttr:
    if value in API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_PARTIAL_UPDATE_SIZE_BYTES_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
