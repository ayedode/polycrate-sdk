from typing import Literal

ApiV1PopsArchiveCreateCountryErrorComponentCode = Literal[
    "invalid", "max_length", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_POPS_ARCHIVE_CREATE_COUNTRY_ERROR_COMPONENT_CODE_VALUES: set[ApiV1PopsArchiveCreateCountryErrorComponentCode] = {
    "invalid",
    "max_length",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_pops_archive_create_country_error_component_code(
    value: str,
) -> ApiV1PopsArchiveCreateCountryErrorComponentCode:
    if value in API_V1_POPS_ARCHIVE_CREATE_COUNTRY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_ARCHIVE_CREATE_COUNTRY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
