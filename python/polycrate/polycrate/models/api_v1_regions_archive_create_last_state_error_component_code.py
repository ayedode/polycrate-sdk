from typing import Literal

ApiV1RegionsArchiveCreateLastStateErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_REGIONS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateLastStateErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_regions_archive_create_last_state_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateLastStateErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
