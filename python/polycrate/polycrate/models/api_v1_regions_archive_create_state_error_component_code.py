from typing import Literal

ApiV1RegionsArchiveCreateStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_archive_create_state_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateStateErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
