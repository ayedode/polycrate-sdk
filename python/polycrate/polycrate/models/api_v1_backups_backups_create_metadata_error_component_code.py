from typing import Literal

ApiV1BackupsBackupsCreateMetadataErrorComponentCode = Literal["invalid", "null"]

API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BackupsBackupsCreateMetadataErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_backups_backups_create_metadata_error_component_code(
    value: str,
) -> ApiV1BackupsBackupsCreateMetadataErrorComponentCode:
    if value in API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BACKUPS_BACKUPS_CREATE_METADATA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
