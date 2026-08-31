from typing import Literal

ApiV1BlocksArchiveCreateSupportsHaErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateSupportsHaErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_archive_create_supports_ha_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateSupportsHaErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_SUPPORTS_HA_ERROR_COMPONENT_CODE_VALUES!r}"
    )
