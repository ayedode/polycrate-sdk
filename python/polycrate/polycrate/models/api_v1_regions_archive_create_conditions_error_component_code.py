from typing import Literal

ApiV1RegionsArchiveCreateConditionsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegionsArchiveCreateConditionsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_regions_archive_create_conditions_error_component_code(
    value: str,
) -> ApiV1RegionsArchiveCreateConditionsErrorComponentCode:
    if value in API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGIONS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
