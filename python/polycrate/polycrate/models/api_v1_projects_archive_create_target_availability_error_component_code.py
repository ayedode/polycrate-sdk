from typing import Literal

ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits"
]

API_V1_PROJECTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
}


def check_api_v1_projects_archive_create_target_availability_error_component_code(
    value: str,
) -> ApiV1ProjectsArchiveCreateTargetAvailabilityErrorComponentCode:
    if value in API_V1_PROJECTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROJECTS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
