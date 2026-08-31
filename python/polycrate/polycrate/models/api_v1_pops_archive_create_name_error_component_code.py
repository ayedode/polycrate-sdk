from typing import Literal

ApiV1PopsArchiveCreateNameErrorComponentCode = Literal[
    "invalid", "max_length", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsArchiveCreateNameErrorComponentCode] = {
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pops_archive_create_name_error_component_code(
    value: str,
) -> ApiV1PopsArchiveCreateNameErrorComponentCode:
    if value in API_V1_POPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
