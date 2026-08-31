from typing import Literal

ApiV1BackupsBackupsUpdateSizeBytesErrorComponentCode = Literal["invalid", "max_string_length", "max_value", "min_value"]

API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsUpdateSizeBytesErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
}


def check_api_v1_backups_backups_update_size_bytes_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsUpdateSizeBytesErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_UPDATE_SIZE_BYTES_ERROR_COMPONENT_CODE_VALUES!r}"
    )
